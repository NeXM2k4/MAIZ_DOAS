from matplotlib import rcParams
from matplotlib.pyplot import close
from matplotlib.pyplot import figure
from matplotlib.pyplot import ylim
from matplotlib.pyplot import plot
from matplotlib.pyplot import savefig
from matplotlib.pyplot import show
from matplotlib.pyplot import legend
from matplotlib.pyplot import xlabel
from matplotlib.pyplot import ylabel
from matplotlib.pyplot import title
from matplotlib.pyplot import ion
from matplotlib.animation import FuncAnimation

from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import figure
from matplotlib.pyplot import get_backend
from matplotlib.pyplot import get_current_fig_manager
from matplotlib.pyplot import switch_backend
from matplotlib.pyplot import subplots
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
from matplotlib.pyplot import xlim

#Plt_2D_Upd=Plot 2 Dimentions Updatable.
    #Function to plot a (x,y) points of data with the function to update.
#Parameters:
    #num_plt=number of plots. integer parameter. This parameter indicate the number of plots to drop.
    #plt_dat_x=plot data x. float array of [num_plt][2] dimentions. This parameter has all x points.
    #plt_dat_y=plot data y. float array of [num_plt][2] dimentions. This parameter has all y points.
    #plt_fil=plot file. string parameter. This parameter indicates the place and name to safe the drop plot.
    #plt_tit=plot title. string parameter. This parameter indicates the name to be used for the plot.
    #plt_lab=plot label. string array of [num_plt] dimentions.
    #plt_mrk=plot marks. string array of [num_plt] dimentions.
    #plt_lin=plot linewidth. floar array of [num_plt] dimentions.
    #plt_col=plot color. string array of [num_plt] dimentions.
    #plt_axi=plot axis. string array of [num_plt] dimentions.
    #plt_sav=plot save. boolean parameter.
    #plt_shw=plot show. boolean parameter.
def Plt_2D_Upd(,,num_plt,plt_fil,plt_tit,plt_lab,plt_mrk,plt_lin,plt_col,plt_axi,plt_sav,plt_shw):
    ion()
    rcParams['legend.fontsize']=10
    plt_poi=figure() #plt_poi=plot points.
    ax1=plt_poi.add_subplot(1,1,1)
    for i_num_plt in range(0,num_plt,1): #i_num_plt=i-counter number of plots.
        plot(plt_dat_x[i_num_plt],plt_dat_y[i_num_plt],marker=plt_mrk[i_num_plt],linewidth=plt_lin[i_num_plt],color=plt_col[i_num_plt],label=plt_lab[i_num_plt])
    title(plt_tit)
    xlabel(plt_axi[0])
    ylabel(plt_axi[1])
    legend()
    def update(i):
        ax1.clear()
        ax1.plot(plt_dat_x[i_num_plt],plt_dat_y[i_num_plt],marker=plt_mrk[i_num_plt],linewidth=plt_lin[i_num_plt],color=plt_col[i_num_plt],label=plt_lab[i_num_plt])
    FuncAnimation(fig=plt_poi,func=update,interval=100)
    if plt_sav==True: savefig(plt_fil,bbox_inches='tight')
    if plt_shw==True: show()
    return

#mon_spe_cap=monitor spectra capture.
#Parameters.
	#cap_tim_sta=capture time start.
	#cap_tim_fin=capture time finish.
	#pol_gra=polynomial grade. integer parameter. this parameter indicates the grade of the polynomial to be used on the optical density fit.
	#gas_num=gases number. integer parameter. this parameter indicates the number of gases to fit.
	#gas_cro_sec=gases cross section. this parameter indicates the gases absorption cross section to perform the slant columns densities fit.
	#spc_spe_poi=spectrometer spectrum points.
	#spc_poi_num=spectrum wavelength points number.
	#spe_poi_num=spectrometer wavelength points number.
	#spc_wav_poi=spectrometer wavelength points.
	#spe_wav_poi=spectrum wavelength points.
	#spc_obj=spectrometer objetc. object parameter. this object controlls the espectrometer settings and recollection.
	#per_fit=perform fit. boolean parameter. this parameter indicates if a fit for the slant column densities will be perform.
def mon_spe_cap(cap_tim_sta,cap_tim_fin,pol_gra,gas_num,gas_cro_sec,spc_spe_poi,spc_poi_num,spe_poi_num,spc_wav_poi,spe_wav_poi,spc_obj,per_fit):
	plt_spe_cap=figure() #plt_spe_cap=plot spectrum capture.
	if get_backend()!='TkAgg': switch_backend('TkAgg') 
	plt_spe_cap_upd=None #plt_spe_cap_upd=plot spectra captured update.
	plt_spe_cap_gas_fit=[None]*gas_num #plt_spe_cap_gas_fit=plot spectrum capture gas fit.
	plt_spe_cap_gas_sla=[None]*gas_num #plt_spe_cap_gas_sla=plot spectrum capture gas slant.
	plt_spe_cap_opt_fit=[None]*2 #plt_spe_cap_opt_fit=plot spectrum optical density fit.
	if per_fit==True: 
		plt_spe_cap_gri=plt_spe_cap.add_gridspec(gas_num+1,gas_num+2) #plt_spe_cap_gri=plot spectrum capture grid.
		plt_spe_cap_gri.update(hspace=0.2,wspace=0.2)
		plt_spe_cap_upd=plt_spe_cap.add_subplot(plt_spe_cap_gri[:gas_num,:gas_num+1])
		for i_gas_num in range(0,gas_num,1): #i_gas_num=i-counter gases number.
			plt_spe_cap_gas_fit[i_gas_num]=plt_spe_cap.add_subplot(plt_spe_cap_gri[gas_num,i_gas_num])
		for i_gas_num in range(0,gas_num,1): #i_gas_num=i-counter gases number.
			plt_spe_cap_gas_sla[i_gas_num]=plt_spe_cap.add_subplot(plt_spe_cap_gri[i_gas_num,gas_num+1])
			xlim(left=cap_tim_sta,right=cap_tim_fin) 
		plt_spe_cap_opt_fit[0]=plt_spe_cap.add_subplot(plt_spe_cap_gri[gas_num,gas_num])
		plt_spe_cap_opt_fit[1]=plt_spe_cap.add_subplot(plt_spe_cap_gri[gas_num,gas_num+1])
	else: 		
		plt_spe_cap_gri=plt_spe_cap.add_gridspec(1,1) #plt_spe_cap_gri=plot spectrum capture grid.
		plt_spe_cap_upd=plt_spe_cap.add_subplot(plt_spe_cap_gri[1,1])
	plt_spe_cap_man=get_current_fig_manager() #plt_spe_cap_man=plot spectrum capture manager.
	plt_spe_cap_man.resize(*plt_spe_cap_man.window.maxsize())
	plt_spe_cap.show()
	plt_spe_cap.canvas.draw()
	cap_tim_poi=[] #cap_tim_poi=capture time point.
	gas_sla_poi=[0]*gas_num #gas_sla_poi=gases slant points.
	for i_gas_num in range(0,gas_num,1): gas_sla_poi[i_gas_num]=[] #i_gas_num=i-counter gases number.
	i_cap_set=0 #i_cap_set=i-counter capturing set.
	sto_cap=False #sto_cap=stop capturing.
	while sto_cap==False:	
		print('Capturing set '+str(i_cap_set))
		print('Capturing reference for set '+str(i_cap_set))
		spc_ref_poi=zeros(shape=(spc_poi_num,),dtype=float,order='F') #spc_ref_poi=spectrometer reference points.
		for i_Spc_Sca_Num in range(0,Spc_Sca_Num,1):
			spc_ref_poi=spc_ref_poi+spc_obj.intensities()+40000*exp(-1*((spc_wav_poi-375)/150)**2) 
		print('Capturing offset for set '+str(i_cap_set))
		spc_ofs_poi=zeros(shape=(spc_poi_num,),dtype=float,order='F') #spc_ofs_poi=spectrometer offset points.
		for i_Spc_Sca_Num in range(0,Spc_Sca_Num,1):
			spc_ofs_poi=spc_ofs_poi+spc_obj.intensities() #intensities() 
		sto_set=False #sto_set=stop set.
		while sto_set==False:
			plt_spe_cap_upd.clear()
			if per_fit==True:
				for i_gas_num in range(0,gas_num,1): #i_gas_num=i-counter gases number.
					plt_spe_cap_gas_fit[i_gas_num].clear()
					#plt_spe_cap_gas_sla[i_gas_num].clear()
				plt_spe_cap_opt_fit[0].clear()
				plt_spe_cap_opt_fit[1].clear()
			print('Capturing measurements for set '+str(i_cap_set))
			spc_int_poi=zeros(shape=(spc_poi_num,),dtype=float,order='F') #spc_int_poi=spectrometer intensity points.
			for i_Spc_Sca_Num in range(0,Spc_Sca_Num,1):
				spc_int_poi=spc_int_poi+spc_obj.intensities()+0.75*40000*exp(-1*((spc_wav_poi-375)/150)**2) 
			spc_int_poi=spc_int_poi/Spc_Sca_Num
			plt_spe_cap_upd.plot(spc_wav_poi,spc_int_poi,color='b')
			if per_fit==True:
				spe_ref_poi=zeros(shape=(spe_poi_num,),dtype=float,order='F') #spe_ref_poi=spectrum reference points.
				spe_ofs_poi=zeros(shape=(spe_poi_num,),dtype=float,order='F') #spe_ofs_poi=spectrum offset points.
				spe_int_poi=zeros(shape=(spe_poi_num,),dtype=float,order='F') #spe_int_poi=spectrometer intensity points.
				for i_spe_poi_num in range(0,spe_poi_num,1): #i_spe_poi_num=spectrum points number.
					spe_ref_poi[i_spe_poi_num]=spc_ref_poi[spc_spe_poi[i_spe_poi_num]]
					spe_ofs_poi[i_spe_poi_num]=spc_ofs_poi[spc_spe_poi[i_spe_poi_num]] 
					spe_int_poi[i_spe_poi_num]=spc_int_poi[spc_spe_poi[i_spe_poi_num]]
				spe_ref_poi=spe_ref_poi-spe_ofs_poi
				spe_int_poi=spe_int_poi-spe_ofs_poi
				gas_sla_poi_upd,gas_sla_fit_poi,opt_den_mea_poi,opt_den_pol_poi,opt_den_res_poi=Spe_Fit_Sla_Col(spe_poi_num,spe_wav_poi,spe_int_poi,spe_ref_poi,pol_gra,gas_num,gas_cro_sec) #gas_sla_poi_upd=gases slant point update.	
				act_tim=localtime() #act_tim=actual time.
				cap_tim_poi.append(act_tim[3]+float(act_tim[4]/60)+float(act_tim[5]/3600))
				for i_gas_num in range(0,gas_num,1): #i_gas_num=i-counter gases number.
					gas_sla_poi[i_gas_num].append(gas_sla_poi_upd[i_gas_num])
					plt_spe_cap_gas_fit[i_gas_num].plot(spe_wav_poi,gas_cro_sec[i_gas_num],color='g')
					plt_spe_cap_gas_fit[i_gas_num].plot(spe_wav_poi,gas_sla_fit_poi[i_gas_num],color='y')
					plt_spe_cap_gas_sla[i_gas_num].plot(cap_tim_poi,gas_sla_poi[i_gas_num],color='g')
				plt_spe_cap_opt_fit[0].plot(spe_wav_poi,opt_den_mea_poi,color='g')
				plt_spe_cap_opt_fit[0].plot(spe_wav_poi,opt_den_pol_poi,color='y')
				plt_spe_cap_opt_fit[1].plot(spe_wav_poi,opt_den_mea_poi,color='g')
				plt_spe_cap_opt_fit[1].plot(spe_wav_poi,opt_den_res_poi,color='y')
			plt_spe_cap.canvas.draw()
		if cap_tim_fin<=cap_tim_poi[i_cap_set]:
			sto_cap=True
		i_cap_set=i_cap_set+1
		sleep(10)
	print('Capture time interval finished!!!')
	plt_spe_cap.show()
	return