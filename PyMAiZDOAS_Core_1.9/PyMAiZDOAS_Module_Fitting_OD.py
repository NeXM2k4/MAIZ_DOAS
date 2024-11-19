import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
import PyMAiZDOAS_Module_Read_Write as mod_raw #mod_raw=module read and write.

from numpy import zeros,nan,nan_to_num,poly1d,diag,log
from scipy.signal import butter,sosfilt,filtfilt
from scipy.odr import polynomial,ODR,Data
from scipy.interpolate import splrep,splev
from scipy.optimize import curve_fit
from multiprocessing import Process

def Prepare_Data(spec_mea,wav_fit,spec_fit,wav_abn):
	for wav_n in range(wav_abn[2]):
		wav_a=wav_abn[0]+wav_n
		spec_fit[0][wav_n]=abs((spec_mea[1][wav_a]-spec_mea[0][wav_a])/(spec_mea[2][wav_a]-spec_mea[0][wav_a]))
	spec_fit[0]=log(spec_fit[0])
	#Creating low pass filter
	#b,a=butter(fil_pss,0.05)
	spec_fit[1]=spec_fit[0]
	for fil_ite in range(mod_ipr.Fil_Pss):
		#sos=butter(N=fil_ord,Wn=fil_cff,fs=fil_sr,btype='low',analog=False,output='sos')
		#spec_fit[1]=sosfilt(sos,spec_fit[1])
		b,a=butter(N=mod_ipr.Fil_ORD,Wn=mod_ipr.Fil_CFF,btype='low',analog=False,output='ba')
		spec_fit[1]=filtfilt(b,a,spec_fit[1])
	#Fitting polinomial
	poly_model=polynomial(mod_ipr.Fit_Pol_Gra) 
	data=Data(wav_fit,spec_fit[1])
	odr_obj=ODR(data,poly_model)
	output=odr_obj.run() #running ODR fitting
	poly=poly1d(output.beta[::-1])
	spec_fit[2]=poly(wav_fit)
	#Fast part
	spec_fit[3]=spec_fit[1]-spec_fit[2]
	return spec_fit

def OD_ACS(wav_pnts,iii_gas,acs_mea,scd_gas):
        OD_fast=zeros(shape=(wav_pnts),dtype=float)
        for ii_gas in range(mod_ipr.Fit_Gas_Num): 
            if ii_gas!=iii_gas: 
                OD_fast+=acs_mea[ii_gas]*scd_gas[ii_gas]
        return OD_fast

def Fit_SCD(wav_pnts,wav_fit,spec_fit,acs_gen,acs_mea,acs_sim):
	scd_shft_gss,scd_shft_dwl,scd_shft_upl=[],[],[]
	scd_fit=zeros(shape=(mod_ipr.Fit_Gas_Num,6),dtype=float)
	for i_gas in range(mod_ipr.Fit_Gas_Num): 
		scd_shft_gss.append(1)
		scd_shft_dwl.append(-1e+1)
		scd_shft_upl.append(+1e+1)
	for i_gas in range(mod_ipr.Fit_Gas_Num): 
		scd_shft_gss.append(0)
		scd_shft_dwl.append(-15)
		scd_shft_upl.append(+15)
	for i_gas in range(mod_ipr.Fit_Gas_Num): 
		scd_shft_gss.append(1)
		scd_shft_dwl.append(0.1)
		scd_shft_upl.append(+3)
	def OD_SCD(wav,*g_scd_shft):
		OD_fast=zeros(shape=(wav_pnts),dtype=float)
		g_scd=zeros(shape=(mod_ipr.Fit_Gas_Num),dtype=float)
		g_shft=zeros(shape=(mod_ipr.Fit_Gas_Num),dtype=float)
		g_sqz=zeros(shape=(mod_ipr.Fit_Gas_Num),dtype=float)
		for i_gas in range(mod_ipr.Fit_Gas_Num):
			g_scd[i_gas]=g_scd_shft[i_gas]
			g_shft[i_gas]=g_scd_shft[mod_ipr.Fit_Gas_Num+i_gas]
			g_sqz[i_gas]=g_scd_shft[2*mod_ipr.Fit_Gas_Num+i_gas]
			if 15<g_shft[i_gas]: g_shft[mod_ipr.Fit_Gas_Num+i_gas]=15
			elif g_shft[i_gas]<-15: g_shft[i_gas]=-15
			if 3<g_sqz[i_gas]: g_sqz[i_gas]=3
			elif g_sqz[i_gas]<0.1: g_sqz[i_gas]=0.1
			acs_mea[i_gas]=splev(g_sqz[i_gas]*wav+g_shft[i_gas],acs_gen[i_gas],der=0)
			#acs_mea[i_gas]=acs_gen[i_gas](g_sqz[i_gas]*wav+g_shft[i_gas])
		#print("SCD:",g_scd)
		#print("shift:",g_shft)
		#print("squeze:",g_sqz)
		#print("F")
		OD_fast+=acs_mea[0]*g_scd[0]*1e+42
		for i_gas in range(1,mod_ipr.Fit_Gas_Num): OD_fast+=acs_mea[i_gas]*g_scd[i_gas]*1e+17
		return OD_fast
	try:
		nan_to_num(spec_fit[3],copy=False,nan=0.0,posinf=0.0,neginf=0.0)
		#print("fit list")
		#print(scd_fit)
		scd_opt,scd_cov=curve_fit(OD_SCD,wav_fit,spec_fit[3],p0=scd_shft_gss,method="dogbox",bounds=(scd_shft_dwl,scd_shft_upl),max_nfev=1000,ftol=1e-8,loss="soft_l1") #bounds=(scd_shft_dwl,scd_shft_upl),nan_policy="omit")
		scd_err=diag(scd_cov)
		#print("fit parameters")
		#print(scd_opt)
		#print(scd_err)
		spec_fit[4]=OD_SCD(wav_fit,*scd_opt)
		spec_fit[5]=spec_fit[1]-spec_fit[2]-spec_fit[4]
		scd_opt=scd_opt*1e17
		scd_opt[0]=scd_opt[0]*1e25 #48-17
		for i_gas in range(mod_ipr.Fit_Gas_Num): 
			for sss in range(3): #sss=slant shift squeeze
				scd_fit[i_gas][2*sss]=scd_opt[i_gas+sss*mod_ipr.Fit_Gas_Num]
				scd_fit[i_gas][2*sss+1]=scd_err[i_gas+sss*mod_ipr.Fit_Gas_Num]
			#scd_fit[i_gas][1].append(scd_opt[i_gas+mod_ipr.Fit_Gas_Num])
			#scd_fit[i_gas][2].append(scd_opt[i_gas+2*mod_ipr.Fit_Gas_Num])
			#print(len(scd_fit[i_gas]))
			if scd_opt[i_gas]!=0.0: acs_sim[i_gas]=(spec_fit[3]-OD_ACS(wav_pnts,i_gas,acs_mea,scd_opt))/scd_opt[i_gas] #-spec_fit[5]
			else: acs_sim[i_gas]=0*acs_mea[i_gas]
	except RuntimeError:
		print("Error - curve_fit failed")
		spec_fit[4]=0*spec_fit[3] #OD_SCD(wav_fit,*scd_gss)
		spec_fit[5]=0*spec_fit[3] #spec_fit[3]-spec_fit[4]  
		for i_gas in range(mod_ipr.Fit_Gas_Num): 
			for sss in range(3): #sss=slant shift squeeze
				scd_fit[i_gas][2*sss]=nan
				scd_fit[i_gas][2*sss+1]=nan
			acs_sim[i_gas]=0*acs_mea[i_gas]
	return spec_fit,acs_sim,scd_fit
    
mm_O4=2*15.9999 #Molar mass O4. Float variable. Units in g/mol.
n_avg=6.022e23 #Avogrado's number. Float variable.
R=8.314472 #Ideal gas constant. Float variable. Units in J/(K*mol). 
P_atm=101325 #Presure atmospheric. Float variable. Units in Pa.
T_atm=293.20616 #Presure atmospheric. Float variable. Units in Pa.
nO4_atm=0.5*mm_O4*(P_atm/(R*T_atm))
#n=(903876.43*nO4)/(8.314472*293.20616)
#Parameter.
    #n_gas=Number gases. int variable. No units.
    #con_gas=
def Est_Con(scd_fit,con_fit):
    con_fit[0].append(nO4_atm)
    for i_gas in range(1,mod_ipr.Fit_Gas_Num): 
        c_gas=(scd_fit[i_gas]/scd_fit[0])*nO4_atm
        con_fit[i_gas].append(c_gas)
    return
