import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
from PyMAiZDOAS_Module_Register import Dte_Upt,Tim_Upt,Tim_Upt_Int,His_Upt,Tim_Mea_Sta,Tim_HMS_Dec_Con,Mea_Fol,Tim_Mea_Sta
from PyMAiZDOAS_Module_Spectrometer import Wav_Cap_Spc,Itn_Cap_Spc,Spc_Ini,Spe_Cap_Spc
from PyMAiZDOAS_Module_ServoController import Srv_Ini,Srv_Tar
from PyMAiZDOAS_Module_CaptureSpectra import Mea_DtB_Ini,Cap_Off,Cap_Ref,Cap_RST,Cap_Mea,Fit_Mea
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
    tim_fin=Tim_HMS_Dec_Con(mod_ipr.Cap_Tim_Fin) #tim_fin=time to finish.
    dtm_wav,dtf_wav,dtf_tim,dtm_orm,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd,dtf_con=Mea_DtB_Ini(mea_his_fil,mea_dte,spc_act,spe_sfn,fit_sfn)
    plt_obj=Plt_Mea_Man_Ini(dtm_wav,dtm_orm,dtf_tim,dtf_wav,dtf_oms,dtf_acs,dtf_scd,dtf_con) #fig_mea=figure measurement. axs_itn=axes intensities. axs_oms=axes optical density measurement simulated. axs_acs=axes absorption cross section. axs_scd=axes slant column densities. axs_con=axes concentrations.
    while(mea_stp==False):
        His_Upt(mea_his_fil,1,'Performing set measurement '+str(mea_set)+' ...')
        dtm_orm[0],tim_off=Cap_Off(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,srv_ctr,mea_dir_pth[2],'Offset')
        plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim,dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[0][0],dtf_con[0][0],fit_sfn,0,plt_obj,0,0,'Offset for set '+str(mea_set))
        dtm_orm[1],tim_ref=Cap_Ref(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,srv_ctr,mea_dir_pth[3],'Reference_Normal')
        plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim,dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[0][0],dtf_con[0][0],fit_sfn,1,plt_obj,0,0,'Reference normal for set '+str(mea_set))
        if mod_ipr.Sol_Trk_Act==True:
            dtm_orm[1],tim_rst=Cap_RST(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,srv_ctr,mea_dir_pth[3],'Reference_Sun_Tracking')
            plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim,dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd,dtf_con,fit_sfn,1,plt_obj,0,0,'Reference sun tracking for set '+str(mea_set))
        for i_ele_pul in range(0,mod_ipr.Ele_Ang_Num,2): #i_ele_pul=i-counter elevation pulse.
            for i_azi_pul in range(0,mod_ipr.Azi_Ang_Num,1): #i_azi_apul=i-counter azimutal pulse.
                Srv_Tar(mea_his_fil,srv_ctr,[i_azi_pul,i_ele_pul,i_ele_pul])
                dtm_orm[2],mea_tim=Cap_Mea(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,mea_dir_pth[1],i_azi_pul,i_ele_pul)
                dtf_tim[0][i_ele_pul][i_azi_pul].append(mea_tim[0])
                dtf_tim[1][i_ele_pul][i_azi_pul].append(mea_tim[1])
                plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim[1][i_ele_pul][i_azi_pul],dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[i_ele_pul][i_azi_pul],dtf_con[i_ele_pul][i_azi_pul],fit_sfn,2,plt_obj,i_azi_pul,i_ele_pul,'Measurement [Azi='+str(mod_ipr.Azi_Ang_Val[i_azi_pul])+','+'Ele='+str(mod_ipr.Ele_Ang_Val[i_ele_pul])+'] for set '+str(mea_set))
                dtf_oms,dtf_acs[1],dtf_scd=Fit_Mea(mea_his_fil,mea_cnt_fil,mea_dir_pth,mea_set,i_azi_pul,i_ele_pul,mea_tim,fit_sfn,dtf_wav,dtm_orm,dtf_oms,dtf_acs,dft_acs_gen,dtf_scd,dtf_con)
                plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim[1][i_ele_pul][i_azi_pul],dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[i_ele_pul][i_azi_pul],dtf_con[i_ele_pul][i_azi_pul],fit_sfn,3,plt_obj,i_azi_pul,i_ele_pul,'Fitting [Azi='+str(mod_ipr.Azi_Ang_Val[i_azi_pul])+','+'Ele='+str(mod_ipr.Ele_Ang_Val[i_ele_pul])+'] for set '+str(mea_set))
            for i_azi_pul in range(1,mod_ipr.Azi_Ang_Num+1,1): #i_azi_apul=i-counter azimutal pulse.
                Srv_Tar(mea_his_fil,srv_ctr,[mod_ipr.Azi_Ang_Num-i_azi_pul,i_ele_pul+1,i_ele_pul+1])
                dtm_orm[2],mea_tim=Cap_Mea(mea_his_fil,mea_cnt_fil,dtm_wav,mea_dte,mea_set,spc_act,spe_sfn,mea_dir_pth[1],mod_ipr.Azi_Ang_Num-i_azi_pul,i_ele_pul+1)
                dtf_tim[0][i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul].append(mea_tim[0])
                dtf_tim[1][i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul].append(mea_tim[1])
                plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim[1][i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul],dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul],dtf_con[i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul],fit_sfn,2,plt_obj,mod_ipr.Azi_Ang_Num-i_azi_pul,i_ele_pul+1,'Measurement [Azi='+str(mod_ipr.Azi_Ang_Val[mod_ipr.Azi_Ang_Num-i_azi_pul])+','+'Ele='+str(mod_ipr.Ele_Ang_Val[i_ele_pul+1])+'] for set '+str(mea_set))
                dtf_oms,dtf_acs[1],dtf_scd=Fit_Mea(mea_his_fil,mea_cnt_fil,mea_dir_pth,mea_set,mod_ipr.Azi_Ang_Num-i_azi_pul,i_ele_pul+1,mea_tim,fit_sfn,dtf_wav,dtm_orm,dtf_oms,dtf_acs,dft_acs_gen,dtf_scd,dtf_con)
                plt_obj=Plt_Mea_Man_Upd(dtm_wav,dtm_orm,dtf_tim[1][i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul],dtf_wav,dtf_oms,dft_acs_gen,dtf_acs,dtf_scd[i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul],dtf_con[i_ele_pul+1][mod_ipr.Azi_Ang_Num-i_azi_pul],fit_sfn,3,plt_obj,mod_ipr.Azi_Ang_Num-i_azi_pul,i_ele_pul+1,'Fitting [Azi='+str(mod_ipr.Azi_Ang_Val[mod_ipr.Azi_Ang_Num-i_azi_pul])+','+'Ele='+str(mod_ipr.Ele_Ang_Val[i_ele_pul+1])+'] for set '+str(mea_set))
        tim_act=Tim_HMS_Dec_Con(Tim_Upt_Int()) #tim_act=time actual.
        if tim_fin<=tim_act: mea_stp=True
        else: mea_set=mea_set+1
    His_Upt(mea_his_fil,0,'Measurements finished!!!')
    print('Measurement finished succesfully!!!')
