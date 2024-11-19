import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
from PyMAiZDOAS_Module_Register import His_Upt

from usb.core import find
from sys import exit
from numpy import array,zeros
import seabreeze
seabreeze.use("pyseabreeze")
from seabreeze.spectrometers import Spectrometer,list_devices

#Wav_Fit_Spc=Wavelengths Fitted by the Spectrometer.
	#This function return the wavelengths capturated using the spectrometer.
#Parameters. 
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_sfn=spectral start finish number. Integer array of [3] dimention. This parameter indicates the start, finish and number of points in the spectral window.
def Wav_Fit_Spc(his_fil,spc_dev,spe_sfn):
	spe_dat_wav=None #spe_dat_wav=spectral data wavelengths.
	if mod_ipr.Fit_SCD==True: 
		spe_sfn=Spc_Win_Ran(his_fil,spc_dev)
		spe_dat_wav=zeros(shape=(spe_sfn[2]),dtype=float,order='F') #spe_dat_wav=spectral data wavelengths.
	spe_dat_cap=spc_dev.wavelengths() #spe_dat_cap=spectral data capturated.
	if mod_ipr.Fit_SCD==True:
		i_wav_cap=0 #i_wav_cap=i-counter wavelength capturated.
		for j_wav_cap in range(spe_sfn[0],spe_sfn[1],1): #j_wav_cap=j-counter wavelength capturated.
			spe_dat_wav[i_wav_cap]=spe_dat_cap[j_wav_cap]
			i_wav_cap=i_wav_cap+1
	else: 
		spe_dat_wav=spe_dat_cap
	return spe_dat_wav

#Itn_Fit_Spc=Intensity Fitted by the Spectrometer.
	#This function return the intensities capturated using the spectrometer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_sfn=spectral start finish number. Integer array of [3] dimention. This parameter indicates the start, finish and number of points in the spectral window.
def Itn_Cap_Spc(his_fil,spc_dev,spe_sfn):
	spe_dat_int=None #spe_dat_int=spectral data intensities.
	if mod_ipr.Fit_SCD==True: spe_dat_int=zeros(shape=(2,spe_sfn[2]),dtype=float,order='F') #spe_dat_int=spectral data intensities.
	spe_dat_cap=spc_dev.intensities() #spe_dat_cap=spectral data capturated.
	if mod_ipr.Fit_SCD==True:
		i_wav_cap=0 #i_wav_cap=i-counter wavelength capturated.
		for j_wav_cap in range(spe_sfn[0],spe_sfn[1],1): #j_wav_cap=j-counter wavelength capturated.
			spe_dat_int[i_wav_cap]=spe_dat_cap[j_wav_cap]
			i_wav_cap=i_wav_cap+1
	else: 
		spe_dat_int=spe_dat_cap
	return spe_dat_int

#Spe_Fit_Spc=Spectrum Fitted by the Spectrometer.
	#This function return the wavelengths and intensities capturated using the spectrometer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_sfn=spectral start finish number. Integer array of [3] dimention. This parameter indicates the start, finish and number of points in the spectral window.
def Spe_Fit_Spc(his_fil,spc_dev,spe_sfn):
	spe_dat_wan=None #spe_dat_wan=spectral data wanted.
	if mod_ipr.Fit_SCD==True: spe_dat_wan=zeros(shape=(2,spe_sfn[2]),dtype=float,order='F') #spe_dat_wan=spectral data wanted.
	spe_dat_cap=[spc_dev.wavelengths(),spc_dev.intensities()] #spe_dat_cap=spectral data capturated.
	if mod_ipr.Fit_SCD==True:
		i_wav_cap=0 #i_wav_cap=i-counter wavelength capturated.
		for j_wav_cap in range(spe_sfn[0],spe_sfn[1],1): #j_wav_cap=j-counter wavelength capturated.
			spe_dat_wan[0][i_wav_cap]=spe_dat_cap[0][j_wav_cap]
			spe_dat_wan[1][i_wav_cap]=spe_dat_cap[1][j_wav_cap]
			i_wav_cap=i_wav_cap+1
	else: 
		spe_dat_wan[0]=spe_dat_cap[0]
		spe_dat_wan[1]=spe_dat_cap[1]
	return spe_dat_wan

#Wav_Cap_Spc=Wavelengths Captured by the Spectrometer.
	#This function return the wavelengths capturated using the spectrometer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_sfn=spectral start finish number. Integer array of [3] dimention. This parameter indicates the start, finish and number of points in the spectral window.
def Wav_Cap_Spc(his_fil,spc_dev,spe_sfn):
	spe_dat_wav=zeros(shape=(spc_dev.pixels),dtype=float,order='F') #spe_dat_wav=spectral data wavelengths.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True: spe_dat_wav=zeros(shape=(2,spe_sfn[2]),dtype=float,order='F') #spe_dat_wav=spectral data wavelengths.
	spe_dat_cap=spc_dev.wavelengths() #spe_dat_cap=spectral data capturated.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True:
		i_wav_cap=0 #i_wav_cap=i-counter wavelength capturated.
		for j_wav_cap in range(spe_sfn[0],spe_sfn[1],1): #j_wav_cap=j-counter wavelength capturated.
			spe_dat_wav[i_wav_cap]=spe_dat_cap[j_wav_cap]
			i_wav_cap=i_wav_cap+1
	else: 
		spe_dat_wav=spe_dat_cap
	return spe_dat_wav

#Itn_Cap_Spc=Intensity Captured by the Spectrometer.
	#This function return the intensities capturated using the spectrometer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_sfn=spectral start finish number. Integer array of [3] dimention. This parameter indicates the start, finish and number of points in the spectral window.
def Itn_Cap_Spc(his_fil,spc_dev,spe_sfn):
	spe_dat_int=zeros(shape=(spc_dev.pixels),dtype=float,order='F') #spe_dat_int=spectral data intensities.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True: spe_dat_int=zeros(shape=(2,spe_sfn[2]),dtype=float,order='F') #spe_dat_int=spectral data intensities.
	spe_dat_cap=spc_dev.intensities() #spe_dat_cap=spectral data capturated.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True:
		i_wav_cap=0 #i_wav_cap=i-counter wavelength capturated.
		for j_wav_cap in range(spe_sfn[0],spe_sfn[1],1): #j_wav_cap=j-counter wavelength capturated.
			spe_dat_int[i_wav_cap]=spe_dat_cap[j_wav_cap]
			i_wav_cap=i_wav_cap+1
	else: 
		spe_dat_int=spe_dat_cap
	return spe_dat_int

#Spe_Cap_Spc=Spectrum Captured by the Spectrometer.
	#This function return the wavelengths and intensities capturated using the spectrometer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
	#spe_sfn=spectral start finish number. Integer array of [3] dimention. This parameter indicates the start, finish and number of points in the spectral window.
def Spe_Cap_Spc(his_fil,spc_dev,spe_sfn):
	spe_dat_wan=zeros(shape=(2,spc_dev.pixels),dtype=float,order='F') #spe_dat_wan=spectral data wanted.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True: spe_dat_wan=zeros(shape=(2,spe_sfn[2]),dtype=float,order='F') #spe_dat_wan=spectral data wanted.
	spe_dat_cap=[spc_dev.wavelengths(),spc_dev.intensities()] #spe_dat_cap=spectral data capturated.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True:
		i_wav_cap=0 #i_wav_cap=i-counter wavelength capturated.
		for j_wav_cap in range(spe_sfn[0],spe_sfn[1],1): #j_wav_cap=j-counter wavelength capturated.
			spe_dat_wan[0][i_wav_cap]=spe_dat_cap[0][j_wav_cap]
			spe_dat_wan[1][i_wav_cap]=spe_dat_cap[1][j_wav_cap]
			i_wav_cap=i_wav_cap+1
	else: 
		spe_dat_wan[0]=spe_dat_cap[0]
		spe_dat_wan[1]=spe_dat_cap[1]
	return spe_dat_wan

#Spc_Win_Ran=Spectrometer Windows Range.
	#This function will indicate the lower and upper limits of the spectral window in the detectable range of the spectrometer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
def Spc_Win_Ran(his_fil,spc_dev):
	spc_wav=spc_dev.wavelengths() #spc_wav=spectrometer wavelengths.
	spc_pix=spc_dev.pixels #spc_pix=spectrometer pixels (number).
	spc_win_sta,spc_win_fin,spc_win_num=None,None,0 #spc_win_sta=spectrometer window start. spc_win_fin=spectrometer window finish. spc_win_num=spectrometer window number.
	His_Upt(his_fil,1,'Setting start and finish range interval for spectrometer wavelengths in the desire spectral window.')
	if mod_ipr.Spe_Win_Sta<=0 or mod_ipr.Spe_Win_Fin<=0: 
		His_Upt(his_fil,1,'Error bad wavelength window setting. The wavelength window cannot be cero (0) neither negative. Please check wavelength window.')
		exit('Error bad wavelength window setting. The wavelength window cannot be cero (0) neither negative. Please check wavelength window.')
	elif mod_ipr.Spe_Win_Fin<=mod_ipr.Spe_Win_Sta: 
		His_Upt(his_fil,1,'Error bad wavelength window setting. The finish wavelength window cannot be equal or lesser than the starting wavelength window. Please check wavelength window.')
		exit('Error bad wavelength window setting. The finish wavelength window cannot be equal or lesser than the starting wavelength window. Please check wavelength window.')
	for i_spc_pix in range(0,spc_pix,1): #i_spc_pix=i-counter spectrometer pixels.
		if mod_ipr.Spe_Win_Sta<=spc_wav[i_spc_pix]: 
			spc_win_sta=i_spc_pix
			break
	if spc_win_sta==None:
		His_Upt(his_fil,1,'Error bad wavelength window setting. The wanted start wavelength window is lower than the minimum detectable wavelength by the spectrometer.')
		exit('Error bad wavelength window setting. The wanted start wavelength window is lower than the minimum detectable wavelength by the spectrometer.')
	for i_spc_pix in range(spc_win_sta,spc_pix,1): #i_spc_pix=i-counter spectrometer pixels.
		if mod_ipr.Spe_Win_Fin<=spc_wav[i_spc_pix]: 
			spc_win_fin=i_spc_pix
			break
		else: spc_win_num=spc_win_num+1
	mod_ipr.Spe_Fit_Num=spc_win_num
	if spc_win_fin==None: 
		His_Upt(his_fil,1,'Error bad wavelength window setting. The wanted finish wavelength window is higher than the maximum detectable wavelength by the spectrometer.')
		exit('Error bad wavelength window setting. The wanted finish wavelength window is higher than the maximum detectable wavelength by the spectrometer.')
	return [spc_win_sta,spc_win_fin,spc_win_num]

#Spc_Fnd=Spectrometer Finder.
	#This function will found all USB spectrometer devices conected to the computer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
def Spc_Fnd(his_fil):
	His_Upt(his_fil,1,'Searching for USB spectrometer devices...')
	spc_dev_lst=list_devices() #spc_dev_lst=spectrometer devices list.
	if len(spc_dev_lst)==0: 
		His_Upt(his_fil,1,'Search compleated. Error, no spectrometer USB devices were found!!!')
		His_Upt(his_fil,1,'Please check USB conections. Measurements collection will be stopped.')
		exit('Error no USB spectrometer device detected. Please check concections.')
	else:
		His_Upt(his_fil,1,'Search compleated. The following spectrometer devices have been found:')
		His_Upt(his_fil,2,'#'+'\t'+'USB spectrometer Device')
		for i_spc_dev in range(0,len(spc_dev_lst),1): His_Upt(his_fil,2,str(i_spc_dev)+'\t'+str(spc_dev_lst[i_spc_dev]))
	return spc_dev_lst

#Spc_Sel=Find Spectrometer.
	#This function will found all USB spectrometer devices conected to the computer.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_lst=spectrometer devices list. String array [n] parameter. This parameter include all the founded USB spectrometers.
def Spc_Sel(his_fil,spc_dev_lst):
	His_Upt(his_fil,1,'Checking for the required USB spectrometer devices from the founded devices list...') 
	spc_dev_mth=False #spc_dev_mth=spectrometer device match.
	spc_dev_fnd=None #spc_dev_fnd=spectrometer device founded.
	for i_spc_dev in range(0,len(spc_dev_lst),1): #i_spc_dev=i-counter spectrometer devices.
		spc_dev_tst=Spectrometer(spc_dev_lst[i_spc_dev]) #spc_dev_tst=spectrometer device test.
		if spc_dev_tst.serial_number==mod_ipr.Spc_Lab_Ser:
			His_Upt(his_fil,1,'Check compleated. The required USB spectrometer device '+spc_dev_tst.serial_number+' was selected.')
			spc_dev_mth=True
			spc_dev_fnd=spc_dev_tst
			break
	if spc_dev_mth==False:
		His_Upt(his_fil,1,'Check compleated. Error, the required USB spectrometer device '+mod_ipr.Spc_Lab_Ser+' was not found!!!.')
		His_Upt(his_fil,1,'Check if the device is correctly conected. Measurements collection will be stopped.')
		exit('Error. USB spectrometer device '+mod_ipr.Spc_Lab_Ser+' was not detected. Please check concections. Measurements collection will be stopped.')
	return spc_dev_fnd

#Spc_Set=Spectrometer Settings.
	#This function set the wanted USB spectrometer device configuration.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#spc_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
def Spc_Set(his_fil,spc_dev_use):
	His_Upt(his_fil,1,'Setting '+spc_dev_use.serial_number+' USB spectrometer device integration time...')
	spc_dev_tim_lim=spc_dev_use.integration_time_micros_limits
	if mod_ipr.Spc_Ite_Tim>spc_dev_tim_lim[1]:
		His_Upt(his_fil,1,'Set compleated. Error, integration time set by the user is too long for '+spc_dev_use.serial_number+' USB spectrometer device. Measurements collection will be stopped.')
		exit('Error. Integration time set by the user is too long for the choosen USB spectrometer device.')
	elif mod_ipr.Spc_Ite_Tim<spc_dev_tim_lim[0]:
		His_Upt(his_fil,1,'Set compleated. Error, integration time set by the user is too short for '+spc_dev_use.serial_number+' USB spectrometer device. Measurements collection will be stopped.')
		exit('Error. Integration time set by the user is too short for the choosen USB spectrometer device.')
	else:
		spc_dev_use.integration_time_micros(mod_ipr.Spc_Ite_Tim)
		His_Upt(his_fil,1,'Set compleated. '+spc_dev_use.serial_number+' USB spectrometer device integration time configured to '+str(mod_ipr.Spc_Ite_Tim)+' micro-seconds.')
	return spc_dev_use

#Spc_Ini=Spectrometer Initialize.
	#This function set the configurations of the desired USB spectrometer to initiate the measurements.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
def Spc_Ini(his_fil):
	His_Upt(his_fil,0,'*****Checking USB spectrometer devices*****') 	
	spc_fnd_lst=Spc_Fnd(his_fil) #spc_fnd_lst=spectrometer founded list.
	spc_dev_obj=Spc_Sel(his_fil,spc_fnd_lst) #spc_dev_obj=spectrometer device object.
	spc_dev_obj=Spc_Set(his_fil,spc_dev_obj)
	spe_rng_sfn=[None,None,None] #spe_rng_sfn=spectral range start finish number.
	spe_win_sfn=[None,None,None] #spe_win_sfn=spectral window start finish number.
	if mod_ipr.Dat_Sto_Spe_Win_Onl==True: spe_rng_sfn=Spc_Win_Ran(his_fil,spc_dev_obj)
	else: spe_rng_sfn=[0,spc_dev_obj.pixels,spc_dev_obj.pixels]
	spe_rng_sfn=array(spe_rng_sfn,dtype=int)
	mod_ipr.Spc_Pxl_Num=spe_rng_sfn[2]
	if mod_ipr.Fit_SCD==True:  
		spe_win_sfn=Spc_Win_Ran(his_fil,spc_dev_obj)
		spe_win_sfn=array(spe_win_sfn,dtype=int)
		mod_ipr.Spe_Fit_Num=spe_win_sfn[2]
	#dir(spc_dev_tst)
	#spc_dev_tst.max_intensity
	#spc_dev_tst.minimum_integration_time_micros
	#spc_dev_tst.integration_time_micros(100000)
	#spc_dev_tst.pixels
	#spc_dev_tst.wavelengths
	#spc_dev_tst.intensities
	return spc_dev_obj,spe_rng_sfn,spe_win_sfn
