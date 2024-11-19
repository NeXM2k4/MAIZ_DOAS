import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
import PyMAiZDOAS_Module_Read_Write as mod_raw #mod_raw=module read and write.
from PyMAiZDOAS_Module_Register import Tim_HMS_Dec_Con
#from PyMAiZDOAS_Module_Fitting_OD import Prepare_Data,Fit_SCD,Est_Con

from matplotlib.pyplot import fignum_exists,figure,savefig,show,ion
from numpy import min,max,isnan,isinf
#from matplotlib.pyplot import xlabel,ylabel,xlim,ylim,plot,savefig,subplots,legend,title,ion,get_backend,get_current_fig_manager,switch_backend

#plt_acs_ric=plot absorption cross section reference interpolated comparison.
	#This function will produce a simple plot for the reference and interpolated acs.
#Parameters:
	#plt_wav=plot wavelength. Float array of dimention [2][wav_num[2]]. This parameter has the wavelength values for the reference and interpolated acs. 
	#plt_acs=plot absorption cross section. Float array of dimention [2][wav_num[2]]. This parameter has the acs values for the reference and interpolated acs.
	#plt_lab=
	#plt_fil=
	#plt_dte=
def plt_acs_ric(plt_wav,plt_acs,plt_lab,plt_fil,plt_dte):
    acs_fig=figure(num=plt_lab+'_'+mod_ipr.Plt_ACS_Tit) #acs_fig=absorption cross section figure.
    acs_axs=acs_fig.add_subplot() #acs_axs=absorption cross section axes.
    acs_axs.plot(plt_wav[0],plt_acs[0],linewidth=mod_ipr.Plt_ACS_Lwd[0],marker=mod_ipr.Plt_ACS_Mar[0],color=mod_ipr.Plt_ACS_CRI[0])
    acs_axs.plot(plt_wav[1],plt_acs[1],linewidth=mod_ipr.Plt_ACS_Lwd[1],marker=mod_ipr.Plt_ACS_Mar[1],color=mod_ipr.Plt_ACS_CRI[1])
    acs_axs.set_title(plt_lab+'_'+mod_ipr.Plt_ACS_Tit)
    acs_axs.set_xlabel(mod_ipr.Plt_ACS_Axs[0])
    acs_axs.set_ylabel(mod_ipr.Plt_ACS_Axs[1])
    acs_axs.set_xlim(plt_wav[1][0],plt_wav[1][-1])
    acs_axs.set_ylim(0.9*min(plt_acs[1]),1.1*max(plt_acs[1]))
    acs_axs.legend(mod_ipr.Plt_ACS_LRI,loc=mod_ipr.Plt_ACS_LgP)
    if mod_ipr.Plt_ACS_Sav==True: savefig(fname=plt_fil)#,format=mod_ipr.Plt_ACS_Typ)
    if mod_ipr.Plt_ACS_Shw==True: show() #papertype=mod_ipr.Plt_ACS_Siz,bbox_inches=mod_ipr.Plt_ACS_BBx
    return

#Plt_Rsc_YAx=Plot Rescale Y Axis.
	#This function will rescale the Y axis of a given plot.
#Parameters:
	#plt_num=plot number. Integer parameter. This parameter indicates de number of individual lines (pairs of x,y values) in a given subplot.
	#plt_dat=plot data. Float array of [plt_axs][number of points to plot in plt_axs value] dimention.
	#plt_axs=plot axes. Object axes. This parameter gives the matplotlib.pyplot.axes for plotting.
def Plt_Rsc_YAx(plt_num,plt_dat,plt_axs):
	plt_min,plt_max=[],[] #plt_min=plot minimum. plt_max=plot maximums.
	for i_plt_num in range(0,plt_num,1):
		plt_min.append(min(plt_dat[i_plt_num]))
		plt_max.append(max(plt_dat[i_plt_num]))
	plt_axs.set_ylim(bottom=min(plt_min),top=min(plt_max))
	return plt_axs

#Plt_Mea_Man_Ini=Plot Measurement Mananger Initialization.
	#This function will initialize a plot to manage the measurement acquisition.
    #Parameters:
        #mea_wav=measurement wavelength. Float array of [mod_ipr.Spc_Pxl_Num] dimentions. Unit in nm.
        #mea_orm=spectra offset-reference-measurent. float array of [3][mod_ipr.Spc_Pxl_Num] dimentions. Unit in a.u.
        #fit_tim=measurement time. Float list of [mod_ipr.Mea_set_Num] dimention]. Units in HH:MM.
        #fit_wav=fit wavelenght. Float array of [mod_ipr.Spe_Pxl_Num]. Units in nm.
        #fit_mfsffr=fit measurement-filtered-slow-fast-fit-residue. Float array of [6][mod_ipr.Spe_Pxl_Num]. Units in nm.
        #dat_fit_acs=data and fit absorption cross section. Float array of [2][mod_ipr.Fit_Gas_Num][mod_ipr.Spe_Pxl_Num]. Units in molecules/m^2.
        #fit_scd=fit slant column density. Float list of [mod_ipr.Fit_Gas_Num][mod_ipr.Azi_Ang_Num][mod_ipr.Ele_Ang_Num][mod_ipr.Mea_set_Num] dimentions. Units in molecules/m^2.
        #fit_con=fit concentration. Float list of [mod_ipr.Fit_Gas_Num][mod_ipr.Azi_Ang_Num][mod_ipr.Ele_Ang_Num][mod_ipr.Mea_set_Num] dimentions. Units in molecules/m^3.
def Plt_Mea_Man_Ini(mea_wav,mea_orm,fit_tim,fit_wav,fit_mfsffr,dat_fit_acs,fit_scd,fit_con):
    dat_acs=dat_fit_acs[0] #dat_acs=data absorption cross section. Float array of [mod_ipr.Fit_Gas_Num][mod_ipr.Spe_Pxl_Num]. Units in molecules/m^2.
    fit_acs=dat_fit_acs[1] #fit_acs=fit absorption cross section. Float array of [mod_ipr.Fit_Gas_Num][mod_ipr.Spe_Pxl_Num]. Units in molecules/m^2.
    fig_mea=figure('Measurement control panel') #plt_fig_mea=plot figure measurements.
    fig_mea.clear()
    n_row,m_col=mod_ipr.Fit_Gas_Num,mod_ipr.Fit_Gas_Num
    if mod_ipr.Fit_SCD==True: 
        if mod_ipr.Fit_Con==True: n_row,m_col=n_row+1,m_col+2
        else: n_row,m_col=n_row+1,m_col+1
    grd=fig_mea.add_gridspec(n_row,m_col,wspace=0.75,hspace=0.75)
    #if get_backend()!='TkAgg': switch_backend('TkAgg') 
    axs_orm=None #axs_orm=axis offset reference measurement.
    axs_fit=[] #axs_fit=axes fitted.
    axs_acs=[] #axs_acs=axes gases absorption cross sections.
    axs_scd=[] #axs_acs=axes gases slant column densities.
    axs_con=[] #axs_acs=axes lines gases concentration.
    lin_orm=[] #lin_spec=lines offset-reference-measurement.
    lin_fit=[] #lin_proc=lines (spectra measurement procesed) fit.
    lin_acs_mea=[] #lin_acs_mea=lines gases absorption cross section measurement.
    lin_acs_fit=[] #lin_acs_fit=lines gases absorption cross section fit.
    lin_scd=[] #lin_scd=lines gases slant column densities.
    lin_con=[] #lin_con=lines gases concentration.
    if mod_ipr.Fit_SCD==True or mod_ipr.Fit_Con==True: axs_orm=fig_mea.add_subplot(grd[0:int(mod_ipr.Fit_Gas_Num/2),0:mod_ipr.Fit_Gas_Num])
    else: axs_orm=fig_mea.add_subplot(grd[0:mod_ipr.Fit_Gas_Num,0:mod_ipr.Fit_Gas_Num])
    axs_orm.set_xlabel("Wavelength (nm)")
    axs_orm.set_ylabel("Intensity (counts)")
    spec_clrs=["blue","red","green"]
    spec_lgnd=["Offset","Reference","Measurement"]
    for orm in range(3): #orm=offset reference measurement.
        lin_orm_tmp,=axs_orm.plot(mea_wav,mea_orm[orm],c=spec_clrs[orm],label=spec_lgnd[orm])
        lin_orm.append(lin_orm_tmp)
        axs_orm.legend()
    if mod_ipr.Fit_SCD==True:
        axs_fit=fig_mea.add_subplot(grd[int(mod_ipr.Fit_Gas_Num/2):mod_ipr.Fit_Gas_Num,0:mod_ipr.Fit_Gas_Num]) #(grd[1:n_gas+1,0:n_gas])
        axs_fit.set_xlabel("Wavelength (nm)")
        axs_fit.set_ylabel("Intensity (counts)")
        fit_clrs=["black","gray","magenta","cyan","brown","gold"]
        fit_lgnd=["Measurement","Filtered","Slow","Fast","Fit","Residual"]
        for mfsffr in range(6):
            lin_fit_tmp,=axs_fit.plot(fit_wav,fit_mfsffr[mfsffr],lw=3.0,c=fit_clrs[mfsffr],label=fit_lgnd[mfsffr])
            lin_fit.append(lin_fit_tmp)
            axs_fit.legend()
        for n_gas in range(mod_ipr.Fit_Gas_Num):                 
            ax_tmp=fig_mea.add_subplot(grd[n_row-1,n_gas])
            axs_acs.append(ax_tmp)
            axs_acs[n_gas].set_xlabel("Wavelength (nm)")
            axs_acs[n_gas].set_ylabel(mod_ipr.Fit_Gas_Lab[n_gas]+" ACS (mole/m3")
            axs_acs[n_gas].set_ylim(0.7*min(dat_acs[n_gas]),1.3*max(dat_acs[n_gas]))
            lin_acs_mea_tmp,=axs_acs[n_gas].plot(fit_wav,dat_acs[n_gas],label="database")
            lin_acs_fit_tmp,=axs_acs[n_gas].plot(fit_wav,fit_acs[n_gas],label="fitted")
            lin_acs_mea.append(lin_acs_mea_tmp)
            lin_acs_fit.append(lin_acs_fit_tmp)    
            #axs_acs[z].legend()
        for n_gas in range(mod_ipr.Fit_Gas_Num): 
            ax_tmp=fig_mea.add_subplot(grd[n_gas,mod_ipr.Fit_Gas_Num])
            axs_scd.append(ax_tmp)
            axs_scd[n_gas].set_xlabel("time (hh:mm)")
            axs_scd[n_gas].set_ylabel("SCD (mole/m2)")
            lin_scd_tmp,=axs_scd[n_gas].plot([0],[0],label=mod_ipr.Fit_Gas_Lab[n_gas])
            lin_scd.append(lin_scd_tmp)   
            axs_scd[n_gas].legend()
        if mod_ipr.Fit_Con==True:
            for n_gas in range(mod_ipr.Fit_Gas_Numas): 
                ax_tmp=fig_mea.add_subplot(grd[n_gas+1,mod_ipr.Fit_Gas_Num+1])
                axs_con.append(ax_tmp)
                axs_con[n_gas].set_xlabel("time (hh:mm)")
                axs_con[n_gas].set_ylabel("C (g/m3)")
                lin_con_tmp,=axs_con[n_gas].plot([0],[0],label=mod_ipr.Fit_Gas_Lab[n_gas])
                lin_con.append(lin_con_tmp)   
                axs_con[n_gas].legend()
	#plt_mea_man=get_current_fig_manager() #plt_spe_cap_man=plot spectrum capture manager.
	#plt_mea_man.resize(*fig_mea.window.maxsize())
    fig_mea.show()
    fig_mea.canvas.draw()
    return [fig_mea,[axs_orm,axs_fit,axs_acs,axs_scd,axs_con],[lin_orm,lin_fit,[lin_acs_mea,lin_acs_fit],lin_scd,lin_con]]

#Plt_Mea_Man_Upd=Plot Measurement Mananger Update.
	#This function will update a plot to manage the measurement acquisition.
#Parameters:
    #plt_obj=plot object. This object have the following fig, ax and line matplotlib objects initialize in Plt_Mea_Man_Ini.
        #plt_obj[0]=fig_mea.
        #plt_obj[1]=[axs_orm,axs_fit,axs_acs,axs_scd,axs_con].
        #plt_obj[2]=[lin_orm,lin_fit,[lin_acs_mea,lin_acs_fit],lin_scd,lin_con].
    #mea_wav=measurement wavelength. Float array of [mod_ipr.Spc_Pxl_Num] dimentions. Unit in nm.
    #mea_orm=spectra offset-reference-measurent. float array of [3][mod_ipr.Spc_Pxl_Num] dimentions. Unit in a.u.
    #fit_tim=measurement time. Float list of [mod_ipr.Mea_set_Num] dimention]. Units in HH:MM.
    #fit_wav=fit wavelenght. Float array of [mod_ipr.Spe_Pxl_Num]. Units in nm.
    #fit_mfsffr=fit measurement-filtered-slow-fast-fit-residue. Float array of [6][mod_ipr.Spe_Pxl_Num]. Units in nm.
    #dat_acs=data absorption cross section. Float array of [mod_ipr.Fit_Gas_Num][mod_ipr.Spe_Pxl_Num]. Units in molecules/m^2.
    #fit_acs=fit absorption cross section. Float array of [mod_ipr.Fit_Gas_Num][mod_ipr..Spe_Pxl_Num]. Units in molecules/m^2.
    #fit_scd=fit slant column density. Float list of [mod_ipr.Fit_Gas_Num][mod_ipr.Azi_Ang_Num][mod_ipr.Ele_Ang_Num][mod_ipr.Mea_set_Num] dimentions. Units in molecules/m^2.
    #fit_con=fit concentration. Float list of [mod_ipr.Fit_Gas_Num][mod_ipr.Azi_Ang_Num][mod_ipr.Ele_Ang_Num][mod_ipr.Mea_set_Num] dimentions. Units in molecules/m^3.
def Plt_Mea_Man_Upd(mea_wav,mea_orm,fit_tim,fit_wav,fit_mfsffr,gen_acs,dat_fit_acs,fit_scd,fit_con,fit_sfn,mea_plt,plt_obj,ele_nxd,azi_ndx,mea_ite_lab):
    if fignum_exists('Measurement control panel'):
        if mea_plt==0: 
            plt_obj[2][0][0].set_ydata(mea_orm[0]) 
            print("Offset",max(mea_orm[0]))
        elif mea_plt==1: 
            plt_obj[2][0][1].set_ydata(mea_orm[1]) 
            plt_obj[1][0].set_ylim(0,1.5*max(mea_orm[1]))
            print("Reference",max(mea_orm[1]))
        elif mea_plt==2: 
            plt_obj[2][0][2].set_ydata(mea_orm[2])
            plt_obj[1][0].set_ylim(0,1.5*max(mea_orm[2]))
            print("Measurement",max(mea_orm[2]))
        elif mea_plt==3 and mod_ipr.Fit_SCD==True:
            dat_acs=dat_fit_acs[0] #dat_acs=data absorption cross section. Float array of [mod_ipr.Fit_Gas_Num][mod_ipr.Spe_Pxl_Num]. Units in molecules/m^2.
            fit_acs=dat_fit_acs[1] #fit_acs=fit absorption cross section. Float array of [mod_ipr.Fit_Gas_Num][mod_ipr.Spe_Pxl_Num]. Units in molecules/m^2.
            od_min=0.9*min(fit_mfsffr[0])
            od_max=1.1*max(fit_mfsffr[0])
            #print(od_min,od_max)
            #print(isnan(od_min),isnan(od_max))
            if isnan(od_min) or isinf(od_min): od_min=-1
            if isnan(od_max) or isinf(od_max): od_max=+1
            if od_min==od_max: od_min,od_max=-1,+1
            plt_obj[1][1].set_ylim(od_min,od_max) 
            for mfsffr in range(6): plt_obj[2][1][mfsffr].set_ydata(fit_mfsffr[mfsffr]) 
            for n_gas in range(mod_ipr.Fit_Gas_Num):
                plt_obj[2][2][1][n_gas].set_ydata(fit_acs[n_gas])
                #plt_obj[1][2][n_gas].set_ylim(0.9*min(fit_acs[n_gas]),1.1*max(fit_acs[n_gas]))
                plt_obj[1][3][n_gas].clear()
                plt_obj[1][3][n_gas].set_xlabel("time (hh:mm)")
                plt_obj[1][3][n_gas].set_ylabel("SCD (mole/m2)")
                #print(fit_tim)
                #print(fit_scd[n_gas])
                    #print(fit_tim,fit_scd[n_gas][0])
                plt_obj[2][3][n_gas],=plt_obj[1][3][n_gas].plot(fit_tim,fit_scd[n_gas][0],label=mod_ipr.Fit_Gas_Lab[n_gas])
                plt_obj[1][3][n_gas].legend()
                if mod_ipr.Fit_Con==True:
                    plt_obj[1][4][n_gas].clear()
                    [1][4][n_gas].set_xlabel("time (hh:mm)")
                    plt_obj[1][4][n_gas].set_ylabel("C (g/m3)")
                    plt_obj[2][4][n_gas],=plt_obj[1][4][n_gas].plot(fit_tim,fit_con[n_gas],label=mod_ipr.Fit_Gas_Lab[n_gas])
                    plt_obj[1][4][n_gas].legend
        else:
            plt_obj[2][0][1].set_ydata(mea_orm[0]) 
            plt_obj[2][0][1].set_ydata(mea_orm[1]) 
            plt_obj[2][0][1].set_ydata(mea_orm[2]) 
        plt_obj[0].suptitle(mea_ite_lab)
        plt_obj[0].canvas.draw()
        plt_obj[0].canvas.flush_events()  
        ion()
    else: plt_obj=Plt_Mea_Man_Ini(mea_time,mea_wav,mea_orm,fit_wav,dat_fit_acs,fit_scd,fit_con)
    return plt_obj
