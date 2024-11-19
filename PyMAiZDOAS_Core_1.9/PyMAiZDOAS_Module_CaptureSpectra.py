import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
from PyMAiZDOAS_Module_Register import Tim_Upt,Tim_Upt_Int,Tim_HMS_Dec_Con,His_Upt
from PyMAiZDOAS_Module_Spectrometer import Wav_Fit_Spc,Wav_Cap_Spc,Itn_Cap_Spc,Spe_Cap_Spc,Spc_Ini
from PyMAiZDOAS_Module_ServoController import Srv_Tar
from PyMAiZDOAS_Module_Fitting_ACS import Fit_Pre_Gas_ACS
from PyMAiZDOAS_Module_Fitting_OD import Prepare_Data,Fit_SCD,Est_Con,Est_Con
from PyMAiZDOAS_Module_Read_Write import Spe_Cap_Sav,Con_Sav,Fit_SCD_Sav,Fit_Con_Sav,Fit_OD_Sav
from PyMAiZDOAS_Module_Sun_Tracking import Solar_Position

from numpy import zeros
from numpy.random import uniform
from datetime import datetime

#Mea_DtB_Ini=Measurements Data Base Initialization.
	#This function will initialize the data bases needed for the measurements.
#Parameters:
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#mea_dte=measurement date. String parameter. This parameter indicates the date of the measurement.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_wdt=spectral windown data. Float array of [3] dimention. This parameter contains the start (spe_wdt[0]) and finish (spe_wdt[1]) pixel number for the spectral windown. Morover, this variable idicates the number of pixels in that interval (spe_wdt[2]). 
def Mea_DtB_Ini(mea_his_fil,mea_dte,spc_dev_use,spe_wdt,spe_fit):
	dtm_wav=zeros(shape=(mod_ipr.Spc_Pxl_Num),dtype=float,order='F') #dtm_wav=data measurement wavelengths.
	dtm_orm=zeros(shape=(3,mod_ipr.Spc_Pxl_Num),dtype=float,order='F') #dtm_itn=data measurement offset-intensities-reference. 
	#dtm_off=zeros(shape=(mod_ipr.Spc_Pxl_Num),dtype=float,order='F') #dtm_off=data measurement offset. 
	#dtm_ref=zeros(shape=(mod_ipr.Spc_Pxl_Num),dtype=float,order='F') #dtm_ref=data measurement reference. 
	dtm_wav=Wav_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	dtm_orm[0]=Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	dtm_orm[1]=Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	dtm_orm[2]=Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	gen_acs=[] #gen_acs=generator absorption cross section.
	dtf_tim=[[],[]] #mod_ipr.Fit_Gas_Num #dtf_tim=data fit times.
	dtf_scd=[] #dtf_scd=data fitted slant column densities.
	dtf_con=[] #dtf_con=data fitted concentrations.
	for i_ele_ang_num in range(0,mod_ipr.Ele_Ang_Num,1): #i_ele_ang_num-counter elevation angle number.
		for ij in range(2):dtf_tim[ij].append([])
		dtf_scd.append([])
		dtf_con.append([])
		for i_azi_ang_num in range(0,mod_ipr.Azi_Ang_Num,1): #i_azi_ang_num-counter azimutal angle number.
			for ij in range(2):dtf_tim[ij][i_ele_ang_num].append([])
			dtf_scd[i_ele_ang_num].append([])
			dtf_con[i_ele_ang_num].append([])
			for i_gas_num in range(0,mod_ipr.Fit_Gas_Num,1): #i_gas_num=i-counter gas number.
				dtf_scd[i_ele_ang_num][i_azi_ang_num].append([])
				dtf_con[i_ele_ang_num][i_azi_ang_num].append([])
				for ijk in range(6): dtf_scd[i_ele_ang_num][i_azi_ang_num][i_gas_num].append([])
				for ij in range(2): dtf_con[i_ele_ang_num][i_azi_ang_num][i_gas_num].append([])
	dtf_wav,dtf_oms,dtf_acs,dtf_wav=None,None,None,None
	if mod_ipr.Fit_SCD==True:
		dtf_wav=zeros(shape=(mod_ipr.Spe_Fit_Num),dtype=float,order='F') #dtf_wav=data fitted wavelengths.
		dtf_oms=zeros(shape=(6,mod_ipr.Spe_Fit_Num),dtype=float,order='F') #2,2 dtb_oms=data fitted optical density measured simulated. 
		dtf_acs=zeros(shape=(2,mod_ipr.Fit_Gas_Num,mod_ipr.Spe_Fit_Num),dtype=float,order='F') #dtf_acs=data fitted absorption cross section.
		dtf_wav=Wav_Fit_Spc(mea_his_fil,spc_dev_use,spe_wdt)
		act_tim=Tim_HMS_Dec_Con(Tim_Upt_Int()) #act_tim=actual time.
		dtf_acs[0],gen_acs=Fit_Pre_Gas_ACS(mea_his_fil,mod_ipr.Spe_Fit_Num,dtf_wav,mea_dte)
		"""
		for i_ele_ang_num in range(0,mod_ipr.Ele_Ang_Num,1): #i_ele_ang_num-counter elevation angle number.
			dtf_acs[1][i_gas_num]=dtf_acs[0][i_gas_num]*(1+0.3*mod_ipr.Spc_Noi_Lvl*uniform(-1,+1))
			for i_azi_ang_num in range(0,mod_ipr.Azi_Ang_Num,1): #i_azi_ang_num-counter azimutal angle number.
				for i_gas_num in range(0,mod_ipr.Fit_Gas_Num,1): #i_gas_num=i-counter gas number.
					dtf_tim[i_ele_ang_num][i_azi_ang_num][i_gas_num].append(act_tim)
					dtf_scd][i_ele_ang_num][i_azi_ang_num][i_gas_num].append(uniform(0,10))
		"""
	return dtm_wav,dtf_wav,dtf_tim,dtm_orm,dtf_oms,gen_acs,dtf_acs,dtf_scd,dtf_con

#Mea_Ref_Off=Measurements Reference Offset.
	#This function will initialize the data bases needed for the measurements.
#Parameters:
	#mea_his_fil=measurement history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#mea_wav=measurement wavelength. Float array. This parameter indicates the wavelength for the capture.
	#mea_dte=measurement date. String parameter. This parameter indicates the date of the measurement.
	#mea_set=measurement set. Integer parameter. This parameter indicates the set number of the measurement.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> object parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_wdt=spectral windown data. Float array of [3] dimention. This parameter contains the start (spe_wdt[0]) and finish (spe_wdt[1]) pixel number for the spectral windown. Morover, this variable idicates the number of pixels in that interval (spe_wdt[2]). 
	#srv_dev_use=servo device used. Object <Spectrometer> object parameter. This parameter is an object for the USB spectrometer configuration.
	#srv_pul_off=servo pulse offset. Integer parameter. This parameter indicates the pulse value to set an angle to measure the offset.
	#dir_ofs=directory offset. String parameter. This parameter indicates the directory to save the measured offset.
	#srv_lab_off=servo label offset. String parameter. This parameter indicates the label for the plotting of the measured offset.
def Cap_Off(mea_his_fil,cnt_fil,mea_wav,mea_dte,mea_set,spc_dev_use,spe_wdt,srv_dev_use,dir_ofs,srv_lab_off):
	His_Upt(mea_his_fil,2,'Performing '+srv_lab_off+' offset for set '+str(mea_set))
	#Srv_Tar(mea_his_fil,srv_dev_use,srv_pul_off)
	srv_dev_use.SrvSetOff(mea_his_fil)
	mea_off=zeros(shape=(spe_wdt[2]),dtype=float,order='F') #mea_off=measurement offser.
	for i_sca_num in range(0,mod_ipr.Spc_Sca_Num,1): # i_sca_num=i-counter spectrum scan number.
		mea_off=mea_off+Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	mea_off=mea_off/mod_ipr.Spc_Sca_Num
	mea_off[1]=(mea_off[2]+mea_off[3])/2
	mea_off[0]=(mea_off[1]+mea_off[2])/2
	off_tim_str=Tim_Upt() #tim_ref=time reference.
	off_tim_cnv=off_tim_str.split(":")
	off_tim_flt=float(off_tim_cnv[0])+float(off_tim_cnv[1])/60+float(off_tim_cnv[2])/3600
	tem_off_ous,tem_off_ins=0,0 #tem_off_ous=temperature offset outside. tem_off_ins=temperature offset inside.
	Con_Sav(mea_his_fil,cnt_fil,[[mea_set],['None'],[srv_lab_off+'/'+str(mod_ipr.Srv_Ele_Ang_Off_Mir)],[off_tim_str],[tem_off_ous],[tem_off_ins]])
	Spe_Cap_Sav(mea_his_fil,[mea_wav,mea_off],spe_wdt[2],dir_ofs,mea_set,srv_lab_off)
	return mea_off,[off_tim_str,off_tim_flt]

#Cap_Ref=Capture Reference.
	#This function will initialize the data bases needed for the measurements.
#Parameters:
	#mea_his_fil=measurement history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#mea_wav=measurement wavelength. Float array. This parameter indicates the wavelength for the capture.
	#mea_dte=measurement date. String parameter. This parameter indicates the date of the measurement.
	#mea_set=measurement set. Integer parameter. This parameter indicates the set number of the measurement.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> object parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_wdt=spectral windown data. Float array of [3] dimention. This parameter contains the start (spe_wdt[0]) and finish (spe_wdt[1]) pixel number for the spectral windown. Morover, this variable idicates the number of pixels in that interval (spe_wdt[2]). 
	#srv_dev_use=servo device used. Object <Spectrometer> object parameter. This parameter is an object for the USB spectrometer configuration.
	#srv_pul_ref=servo pulse reference. Integer parameter. This parameter indicates the pulse value to set an angle to measure the reference.
	#dir_ref=directory reference. String parameter. This parameter indicates the directory to save the measured reference.
	#srv_lab_ref=servo label reference. This parameter indicates the label for the plotting of the measured reference.
def Cap_Ref(mea_his_fil,cnt_fil,mea_wav,mea_dte,mea_set,spc_dev_use,spe_wdt,srv_dev_use,dir_ref,srv_lab_ref):
	His_Upt(mea_his_fil,2,'Performing '+srv_lab_ref+' reference for set '+str(mea_set))
	#Srv_Tar(mea_his_fil,srv_dev_use,srv_pul_ref)
	srv_dev_use.SrvSetRef(mea_his_fil)
	mea_ref=zeros(shape=(spe_wdt[2]),dtype=float,order='F') #mea_ref=measurement reference.
	for i_sca_num in range(0,mod_ipr.Spc_Sca_Num,1): # i_sca_num=i-counter spectrum scan number.
		mea_ref=mea_ref+Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	mea_ref=mea_ref/mod_ipr.Spc_Sca_Num
	mea_ref[1]=(mea_ref[2]+mea_ref[3])/2
	mea_ref[0]=(mea_ref[1]+mea_ref[2])/2
	ref_tim_str=Tim_Upt() #tim_ref=time reference.
	ref_tim_cnv=ref_tim_str.split(":")
	ref_tim_flt=float(ref_tim_cnv[0])+float(ref_tim_cnv[1])/60+float(ref_tim_cnv[2])/3600
	tem_ref_ous,tem_ref_ins=0,0 #tem_off_ous=temperature offset outside. tem_off_ins=temperature offset inside.
	Con_Sav(mea_his_fil,cnt_fil,[[mea_set],['None'],[srv_lab_ref+'/'+str(mod_ipr.Srv_Ele_Ang_Ref)],[ref_tim_str],[tem_ref_ous],[tem_ref_ins]])
	Spe_Cap_Sav(mea_his_fil,[mea_wav,mea_ref],spe_wdt[2],dir_ref,mea_set,srv_lab_ref)
	return mea_ref,[ref_tim_str,ref_tim_flt]

#Cap_RST=Capture Reference Sun Tracking.
	#This function will initialize the data bases needed for the measurements.
#Parameters:
	#mea_his_fil=measurement history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#mea_wav=measurement wavelength. Float array. This parameter indicates the wavelength for the capture.
	#mea_dte=measurement date. String parameter. This parameter indicates the date of the measurement.
	#mea_set=measurement set. Integer parameter. This parameter indicates the set number of the measurement.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> object parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_wdt=spectral windown data. Float array of [3] dimention. This parameter contains the start (spe_wdt[0]) and finish (spe_wdt[1]) pixel number for the spectral windown. Morover, this variable idicates the number of pixels in that interval (spe_wdt[2]). 
	#srv_dev_use=servo device used. Object <Spectrometer> object parameter. This parameter is an object for the USB spectrometer configuration.
	#dir_ref=directory reference. String parameter. This parameter indicates the directory to save the measured reference.
	#srv_lab_ref=servo label reference. This parameter indicates the label for the plotting of the measured reference.
def Cap_RST(mea_his_fil,cnt_fil,mea_wav,mea_dte,mea_set,spc_dev_use,spe_wdt,srv_dev_use,dir_ref,srv_lab_ref):
	His_Upt(mea_his_fil,2,'Performing '+srv_lab_ref+' reference sun tracking for set '+str(mea_set))
	dat_rst=datetime.now() #dat_rst=date and time reference sun tracking.
	rst_azi_ang,rst_ele_ang=Solar_Position(srv_dev_use)
	#if 0<=srv_ang_ref_azi and srv_ang_ref_azi<=mod_ipr.Srv_Azi_Ang_Shf: srv_ang_ref_azi_tse=mod_ipr.Srv_Azi_Ang_Shf-srv_ang_ref_azi
	#elif mod_ipr.Srv_Azi_Ang_Shf<=srv_ang_ref_azi and srv_ang_ref_azi<=mod_ipr.Srv_Azi_Ang_HSh+mod_ipr.Srv_Azi_Ang_Shf: srv_ang_ref_azi_tse=mod_ipr.Srv_Azi_Ang_Min
	#elif mod_ipr.Srv_Azi_Ang_HSh+mod_ipr.Srv_Azi_Ang_Shf<=srv_ang_ref_azi and srv_ang_ref_azi<=2*mod_ipr.Srv_Azi_Ang_HSh+mod_ipr.Srv_Azi_Ang_Shf: srv_ang_ref_azi_tse=mod_ipr.Srv_Azi_Ang_Max
	#else: srv_ang_ref_azi_tse=360-srv_ang_ref_azi+mod_ipr.Srv_Azi_Ang_Shf
	srv_dev_use.SrvSetRST(mea_his_fil)
	mea_rst=zeros(shape=(spe_wdt[2]),dtype=float,order='F') #mea_rst=measurement reference sun tracking.
	for i_sca_num in range(0,mod_ipr.Spc_Sca_Num,1): # i_sca_num=i-counter spectrum scan number.
		mea_rst=mea_rst+Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	mea_rst=mea_rst/mod_ipr.Spc_Sca_Num
	mea_rst[1]=(mea_rst[2]+mea_rst[3])/2
	mea_rst[0]=(mea_rst[1]+mea_rst[2])/2
	tim_rst=Tim_Upt() #tim_rst=time reference sun tracking.
	rst_tim_str=Tim_Upt() #tim_ref=time reference.
	rst_tim_cnv=rst_tim_str.split(":")
	rst_tim_flt=float(rst_tim_cnv[0])+float(rst_tim_cnv[1])/60+float(rst_tim_cnv[2])/3600
	tem_ref_ous,tem_ref_ins=0,0 #tem_off_ous=temperature offset outside. tem_off_ins=temperature offset inside.
	Con_Sav(mea_his_fil,cnt_fil,[[mea_set],[srv_lab_ref+'/'+str(int(rst_azi_ang))],[srv_lab_ref+'/'+str(int(rst_ele_ang))],[rst_tim_cnv],[tem_ref_ous],[tem_ref_ins]])
	Spe_Cap_Sav(mea_his_fil,[mea_wav,mea_rst],spe_wdt[2],dir_ref,mea_set,srv_lab_ref)
	return mea_rst,[rst_tim_str,rst_tim_flt]

#Cap_Mea=Measurements Reference Offset.
	#This function will initialize the data bases needed for the measurements.
#Parameters:
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#mea_dte=measurement date. String parameter. This parameter indicates the date of the measurement.
	#mea_set=measurement set. Integer parameter. This parameter indicates the set number of the measurement.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_wdt=spectral windown data. Float array of [3] dimention. This parameter contains the start (spe_wdt[0]) and finish (spe_wdt[1]) pixel number for the spectral windown. Morover, this variable idicates the number of pixels in that interval (spe_wdt[2]). 
	#srv_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
def Cap_Mea(mea_his_fil,cnt_fil,mea_wav,mea_dte,mea_set,spc_dev_use,spe_wdt,dir_int,srv_azi_ang,srv_ele_ang):
	mea_int=zeros(shape=(spe_wdt[2]),dtype=float,order='F') #mea_int=measurement intensity.
	for i_sca_num in range(0,mod_ipr.Spc_Sca_Num,1): # i_sca_num=i-counter spectrum scan number.
		mea_int=mea_int+Itn_Cap_Spc(mea_his_fil,spc_dev_use,spe_wdt)
	mea_int=mea_int/mod_ipr.Spc_Sca_Num
	mea_int[1]=(mea_int[2]+mea_int[3])/2
	mea_int[0]=(mea_int[1]+mea_int[2])/2
	mea_tim_str=Tim_Upt() #tim_ref=time reference.
	mea_tim_cnv=mea_tim_str.split(":")
	mea_tim_flt=float(mea_tim_cnv[0])+float(mea_tim_cnv[1])/60+float(mea_tim_cnv[2])/3600
	mea_lab='Azi_'+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+'_Ele_'+str(mod_ipr.Ele_Ang_Val[srv_ele_ang]) #mea_lab=measurement label.
	His_Upt(mea_his_fil,2,'Performing measurement for Azimutal: '+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+' at Elevation '+str(mod_ipr.Ele_Ang_Val[srv_ele_ang])+'...')
	mea_tem_ous,mea_tem_ins=0,0 #mea_tem_ous=measurement temperature outside. mea_tem_ins=measurement temperature inside.
	Con_Sav(mea_his_fil,cnt_fil,[[mea_set],[mod_ipr.Azi_Ang_Val[srv_azi_ang]],[mod_ipr.Ele_Ang_Val[srv_ele_ang]],[mea_tim_str],[mea_tem_ous],[mea_tem_ins]])
	Spe_Cap_Sav(mea_his_fil,[mea_wav,mea_int],spe_wdt[2],dir_int,mea_set,mea_lab)
	return mea_int,[mea_tim_str,mea_tim_flt]

#Fit_Mea=Measurements Reference Offset.
	#This function will initialize the data bases needed for the measurements.
#Parameters:
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#mea_dte=measurement date. String parameter. This parameter indicates the date of the measurement.
	#mea_set=measurement set. Integer parameter. This parameter indicates the set number of the measurement.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_wdt=spectral windown data. Float array of [3] dimention. This parameter contains the start (spe_wdt[0]) and finish (spe_wdt[1]) pixel number for the spectral windown. Morover, this variable idicates the number of pixels in that interval (spe_wdt[2]). 
	#srv_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
def Fit_Mea(mea_his_fil,mea_cnt_fil,mea_pth,mea_set,srv_azi_ang,srv_ele_ang,mea_tim,fit_sfn,fit_wav,mea_orm,fit_oms,dat_fit_acs,gen_acs,fit_scd,fit_con):
	if mod_ipr.Fit_SCD==True:
		His_Upt(mea_his_fil,2,'Saving fitting for Azimutal: '+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+' at Elevation '+str(mod_ipr.Ele_Ang_Val[srv_ele_ang])+'...')
		dat_acs,fit_acs=dat_fit_acs[0],dat_fit_acs[1]
		fit_oms=Prepare_Data(mea_orm,fit_wav,fit_oms,fit_sfn)
		fit_oms,fit_acs,fit_scd_act=Fit_SCD(fit_sfn[2],fit_wav,fit_oms,gen_acs,dat_acs,fit_acs)
		for i_gas in range(mod_ipr.Fit_Gas_Num): 
			for sss in range(6): #sss=slant shift squeeze
				fit_scd[srv_ele_ang][srv_azi_ang][i_gas][sss].append(fit_scd_act[i_gas][sss])
		mea_lab='Azi_'+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+'_Ele_'+str(mod_ipr.Ele_Ang_Val[srv_ele_ang]) #mea_lab=measurement label.
		scd_fil=mea_pth[6]+"SCD"+"_"+str(mod_ipr.Ele_Ang_Val[srv_ele_ang])+"_"+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+"."+mod_ipr.Dat_SCD_Typ
		print(mea_tim)
		Fit_SCD_Sav(scd_fil,mea_tim,fit_scd_act)
		od_fil=mea_pth[4]+"OD_Set_"+str(mea_set)+"_"+str(mod_ipr.Ele_Ang_Val[srv_ele_ang])+"_"+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+"."+mod_ipr.Dat_FOD_Typ
		Fit_OD_Sav(od_fil,fit_sfn[2],fit_wav,fit_oms,dat_acs,fit_acs)
		if mod_ipr.Fit_Con==True:
			Est_Con(fit_scd,fit_con)
			con_fil=mea_pth[6]+"Con"+"_"+str(mod_ipr.Ele_Ang_Val[srv_ele_ang])+"_"+str(mod_ipr.Azi_Ang_Val[srv_azi_ang])+"."+mod_ipr.Dat_Con_Typ
			Fit_Con_Sav(con_fil,mea_tim,fit_con)
	return fit_oms,fit_acs,fit_scd
