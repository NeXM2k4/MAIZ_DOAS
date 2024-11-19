import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
from PyMAiZDOAS_Module_Register import Dte_Upt,Tim_Upt,Tim_Upt_Int,His_Upt,Tim_Mea_Sta,Tim_HMS_Dec_Con,Mea_Fol,Tim_Mea_Sta
from PyMAiZDOAS_Module_Spectrometer import Wav_Cap_Spc,Itn_Cap_Spc,Spc_Ini,Spe_Cap_Spc
from PyMAiZDOAS_Module_ServoController import Srv_Ini,Srv_Tar
from PyMAiZDOAS_Module_CaptureSpectra import Mea_DtB_Ini,Cap_Off,Cap_Ref,Cap_RST,Cap_Mea
from PyMAiZDOAS_Module_Plotting import Plt_Mea_Man_Ini,Plt_Mea_Man_Upd
from PyMAiZDOAS_Module_Read_Write import Spe_Cap_Sav

from multiprocessing import cpu_count,Process
from time import sleep

#*********************************************
#Initialize directory paths and history file.*
#*********************************************

mea_dte=Dte_Upt() #mea_dte=measurements date.
mea_tim=Tim_Upt() #mea_tim=measurements time.
mea_set,mea_cnt_fil,mea_his_fil,mea_dir_pth=Mea_Fol(mea_dte,mea_tim) #mea_set=measurement set. mea_cnt_fil=measurement control file. mea_his_fil=measurements history file. mea_pth=measurement directories path.

#************************************
#Initialize USB spectrometer device.*
#************************************

spc_act,spe_sfn,fit_sfn=Spc_Ini(mea_his_fil) #spectrometer activated. spe_sfn=spectrum start finish number.

#************************************
#Initialize USB servo-motor devices.*
#************************************

srv_ctr=Srv_Ini(mea_his_fil) #srv_act=servos activated.

print(srv_ctr.srv_azi_pul)
print(srv_ctr.srv_ele_pul)
print(srv_ctr.srv_mir_pul)
"""
i=0
while i<10:	
	for azi in range(mod_ipr.Azi_Ang_Num):
		for ele in range(mod_ipr.Ele_Ang_Num):
			srv_ctr.SrvSet(azi,ele,ele,mea_his_fil)
		srv_ctr.SrvSet(azi,0,0,mea_his_fil)
	for azi in range(1,mod_ipr.Azi_Ang_Num+1):
		for ele in range(mod_ipr.Ele_Ang_Num):
			srv_ctr.SrvSet(mod_ipr.Azi_Ang_Num-azi,ele,ele,mea_his_fil)
		srv_ctr.SrvSet(mod_ipr.Azi_Ang_Num-azi,0,0,mea_his_fil)
	i+=1
""" 

#*************************************************
#Waiting for starting MAiZ-DOAS Measurements time*
#*************************************************

Tim_Mea_Sta(mea_his_fil)

#*****************************
#Start MAyZ-DOAS Measurements*
#*****************************

if __name__ =='__main__':
	#print('Number of CPU cores:',cpu_count())
	His_Upt(mea_his_fil,0,'*****Measurements start*****') 	
	mea_stp=False #mea_stp=measurements stop.
	dtm_wav,dtf_wav,dtf_tim,dtm_orm,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd,dtf_con=Mea_DtB_Ini(mea_his_fil,mea_dte,spc_act,spe_sfn,fit_sfn)
	plt_obj=Plt_Mea_Man_Ini(dtm_wav,dtm_orm,dtf_tim,dtf_wav,dtf_oms,dtf_acs,dtf_scd,dtf_con) #fig_mea=figure measurement. axs_itn=axes intensities. axs_oms=axes optical density measurement simulated. axs_acs=axes absorption cross section. axs_scd=axes slant column densities. axs_con=axes concentrations.
	test_over=0
	while test_over==0:
		i_azi_pul=int(input("select azi angle: "))
		i_ele_pul=int(input("select ele angle: "))
		Srv_Tar(mea_his_fil,srv_ctr,[i_azi_pul,i_ele_pul,i_ele_pul])
		#dtm_orm[0],tim_off=Cap_Mea(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,srv_ctr,mea_dir_pth[2],'Offset')
		dtm_orm[2],mea_tim=Cap_Mea(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,mea_dir_pth[1],i_azi_pul,i_ele_pul)
		Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim,dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[i_ele_pul][i_azi_pul],dtf_con[i_ele_pul][i_azi_pul],fit_sfn,1,plt_obj,i_ele_pul,i_azi_pul,'Offset for set '+str(mea_set))
		print("Finish tes?")
		print("\t Press 0 to continue")
		print("\t Press 1 to stop")
		test_over=int(input("Select option: "))
	input('Press any key to terminate script...')
#"""
