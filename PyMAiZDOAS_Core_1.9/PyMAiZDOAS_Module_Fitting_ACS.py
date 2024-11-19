import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
import PyMAiZDOAS_Module_Read_Write as mod_raw #mod_raw=module read and write.
from PyMAiZDOAS_Module_Plotting import plt_acs_ric

from numpy import zeros,nan_to_num,poly1d,diag
from scipy.signal import butter,sosfilt,filtfilt
from scipy.odr import polynomial,ODR
from scipy.interpolate import splrep,splev
from scipy.optimize import curve_fit
from multiprocessing import Process

#Fit_Pre_Gas_ACS=Fitting Preparation Gases Absorption Cross Section.
#Parameter.
	#wav_req_num=wavelength required number. Integer parameter. This parameter indicates the number of required wavelength.
	#wav_req_val=wavelength required values. Float array of dimention [wav_req_num] array parameter. This parameter contains the values for each required wavelength. 
	#fit_dte=fitting date. String array parameter. This parameter containst the date for the fitting process. This date will be used to locate the respective folder and save the data if the user activate said option.
def Fit_Pre_Gas_ACS(mea_his_fil,wav_req_num,wav_req_val,fit_dte):
	gas_acs_itr=zeros(shape=(mod_ipr.Fit_Gas_Num,wav_req_num),dtype=float,order='F') #gas_acs_itr=gases absorption cross sections interpolated.
	gas_acs_par=[]
	for i_gas_num in range(0,mod_ipr.Fit_Gas_Num,1): #i_gas_num=i-counter gases number. #s=0 #s equal 0 measn no smoothing.
		gas_acs_ref=mod_raw.Rea_Fil_Txt_Flt(mod_ipr.Dir_Rea_Cro_Sec+mod_ipr.Fit_Gas_ACS_Fil[i_gas_num]) #gas_acs_ref=gas absorption cros sections reference. gas_acs_ref[0]==wavelenght. gas_acs_ref[1]==acs. 
		#print(mod_ipr.Dir_Rea_Cro_Sec+mod_ipr.Fit_Gas_ACS_Fil[i_gas_num],len(gas_acs_ref[0]),len(gas_acs_ref[1]))
		gas_acs_par_act=splrep(gas_acs_ref[0],gas_acs_ref[1]) #gas_acs_par=gas absorption cross section parametric.
		gas_acs_par.append(gas_acs_par_act)
		gas_acs_itr[i_gas_num]=splev(wav_req_val,gas_acs_par_act,der=0)
		plt_com_wav=[gas_acs_ref[0],wav_req_val] #plt_com_wav=plot comparison wavelengths.
		plt_com_acs=[gas_acs_ref[1],gas_acs_itr[i_gas_num]] #plt_com_acs=plot comparison absorption cross section.
		com_fil=mod_ipr.Dir_Sav_Mai_Pth+mod_ipr.Dat_Fld_Nam+fit_dte+'/'+mod_ipr.Dir_Sav_Fit_Set+mod_ipr.Fit_Gas_Lab[i_gas_num]+'_'+mod_ipr.Plt_ACS_Tit+'.' #com_fil=comparison file. 
		#print(com_fil)
		#plt_sub_pro=Process(target=plt_acs_ric,args=(plt_com_wav,plt_com_acs,mod_ipr.Fit_Gas_Lab[i_gas_num],com_fil+mod_ipr.Plt_ACS_Typ,fit_dte))
		#plt_sub_pro.start()
		#plt_acs_ric(gas_acs_ref[0],gas_acs_ref[1],mod_ipr.Fit_Gas_Lab[i_gas_num],com_fil+mod_ipr.Plt_ACS_Typ,fit_dte)
		plt_acs_ric(plt_com_wav,plt_com_acs,mod_ipr.Fit_Gas_Lab[i_gas_num],com_fil+mod_ipr.Plt_ACS_Typ,fit_dte)
		mod_raw.Wri_Dat_Str_Txt(com_fil+'txt',mod_ipr.Dat_ACS_CHe,2,2,'w')		
		mod_raw.Wri_WYD_Flt_Txt(com_fil+'txt',[wav_req_val,gas_acs_itr[i_gas_num]],mod_ipr.Dat_ACS_CFi,mod_ipr.Dat_ACS_CFo,2,wav_req_num,'a')
	return gas_acs_itr,gas_acs_par
