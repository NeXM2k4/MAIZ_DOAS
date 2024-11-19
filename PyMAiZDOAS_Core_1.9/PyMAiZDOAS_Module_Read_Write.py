#######################################################################################################
##PyEART Module Read and Write -- Version 1.0                                                        ##
##The funtions on this module are made to read and write data related with the simulation.           ##
#######################################################################################################

import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.

from numpy import zeros

#Cre_Fil_His=Create File History.
#Parameters:
	#his_fil_nam=history file name. String parameter. This parameter indicates the directory and name to create the history file.
	#his_fil_dte=history file date. String parameter. This parameter indicates the date when the history file was created.
	#his_fil_tim=history file time. String parameter. This parameter indicates the time when the history file was created.
def Cre_Fil_His(his_fil_nam,his_fil_dte,his_fil_tim):
	his_fil=open(file=his_fil_nam,mode='w') #his_fil=history file.
	lin_hea='* History file for MA&Z-DOAS (Multi Azimutal & Zenith Differential Optical Absorption Spectroscopy) *' #lin_hea=line header.
	lin_mar=''
	for i_lin_cha in range(0,len(lin_hea),1): lin_mar=lin_mar+'*'
	lin_sta='*****This measurement adquisitions were performed on '+his_fil_dte+' at '+his_fil_tim+'*****' #lin_sta=line start.
	lin_ini='\n'+lin_mar+'\n'+lin_hea+'\n'+lin_mar+'\n\n\n'+lin_sta+'\n\n' #lin_ini=line initialization.
	print(lin_ini)
	his_fil.write(lin_ini)
	his_fil.close()
	return

#His_Fil_Wri=History File Write.
	#This function will write the data given in the history file.
#Parameters.
	#his_fil_nam=history file name. string parameter. This parameter indicates the directory and name of the file to be read.
	#his_msg_str=history file message. string parameter. This parameter indicates the line to be written in the history file.
def His_Fil_Wri(his_fil_nam,his_msg_str):
	his_fil=open(file=his_fil_nam,mode='a') #his_fil=history file.
	his_fil.write(his_msg_str+'\n')
	his_fil.close()
	return

#His_Fil_Mer=History File Merge.
	#This function will merge the data given in the history files.
#Parameters.
	#his_fil_nam=history file names. String array. This parameter indicates the directory and name of the history files to be merged.
	#his_fil_mer=history file merge. String parameter. This parameter indicates the directory and name of the merged history file.
def His_Fil_Mer(his_fil_nam,his_fil_mer):
	with open(his_fil_mer,'w') as his_fil_mer_out: #his_fil_mer_out=history file merged out.
    		for his_fil_nam_act in his_fil_nam: #his_fil_nam_act=history file name actual.
        		with open(his_fil_nam_act) as his_fil_act: #his_fil_act=history file actual.
            			for his_fil_act_lin in his_fil_act: #his_fil_act_lin=history file actual line.
                			his_fil_mer_out.write(his_fil_act_lin)
	return

#Rea_Fil_Txt=Read File Text.
	#This function will open an text file and save its contents in a array.
#Parameters.
	#txt_fil_nam=text file name. string parameter. This parameter indicates the directory and name of the file to be read.
def Rea_Fil_Txt(txt_fil_nam):
	print(txt_fil_nam)
	rea_txt_fil=open(file=txt_fil_nam,mode='r') #rea_txt_fil=read text file.
	rea_dat_num_lin=0 #rea_dat_num_lin=read data number lines.
	rea_dat_num_col=0 #rea_dat_num_col=read data number columns.
	rea_dat=[] #rea_dat=read data x.
	for i_lin in rea_txt_fil: #i_lin=i-counter line.
		cells=i_lin.split()
		rea_dat_num_col=len(cells)
		for i_col in range(0,rea_dat_num_col,1): #i_col=i-counter column.
			rea_dat.append([])
		break
	for i_lin in rea_txt_fil: #i_lin=i-counter line.
		cells=i_lin.split()	
		for i_col in range(0,rea_dat_num_col,1): #i_col=i-counter column.
			rea_dat[i_col].append(cells[i_col])
		rea_dat_num_lin=rea_dat_num_lin+1
	rea_txt_fil.close()
	return rea_dat

#Rea_Fil_Txt=Read File Text.
	#This function will open an text file and save its contents in a array.
#Parameters.
	#txt_fil_nam=text file name. string parameter. This parameter indicates the directory and name of the file to be read.
def Rea_Fil_Txt_Flt(txt_fil_nam):
	print(txt_fil_nam)
	rea_txt_fil=open(file=txt_fil_nam,mode='r') #rea_txt_fil=read text file.
	rea_dat_num_lin=0 #rea_dat_num_lin=read data number lines.
	rea_dat_num_col=0 #rea_dat_num_col=read data number columns.
	rea_dat=[] #rea_dat=read data x.
	for i_lin in rea_txt_fil: #i_lin=i-counter line.
		cells=i_lin.split()
		rea_dat_num_col=len(cells)
		for i_col in range(0,rea_dat_num_col,1): #i_col=i-counter column.
			rea_dat.append([])
		break
	for i_lin in rea_txt_fil: #i_lin=i-counter line.
		cells=i_lin.split()	
		for i_col in range(0,rea_dat_num_col,1): #i_col=i-counter column.
			rea_dat[i_col].append(float(cells[i_col]))
		rea_dat_num_lin=rea_dat_num_lin+1
	rea_txt_fil.close()
	return rea_dat

#Rep_Fil_Txt=Replace File Text.
	#This function will open an text file and save its contents in a array.
#Parameters.
	#txt_fil_nam=text file name. String parameter. This parameter indicates the directory and name of the file to be read.
	#txt_lin_lab= String parameter. This parameter indicates the line which is going to be replaced.
	#txt_lin_rep= String parameter. This parameter indicates the text which is going to be replaced.
def Rep_Fil_Txt(txt_fil_nam,txt_lin_lab,txt_lin_rep):
	ori_txt_fil=open(file=txt_fil_nam,mode='r').read() #rep_txt_fil=replace text file.
	rep_txt=ori_txt_fil.replace(txt_lin_lab,txt_lin_rep)
	rep_ext_fil=open(file=txt_fil_nam,mode='w')
	rep_ext_fil.write(rep_txt)
	rep_ext_fil.close()
	return 

#Wri_Dat_Str_Txt=Write Data String Text.
	#This function will write the data given in a text file.
#Parameters.
	#txt_fil_nam=text file name. string parameter. This parameter indicates the directory and name of the file to be read.
	#wri_dat_val=write data values. float array of [wri_dat_col_num][wri_dat_lin_num] dimentions. This parameter has all the data to write.
	#wri_dat_col_num=write data columns number. integer variable. This parameter indicates the number of columns in the data.
	#wri_dat_lin_num=write data lines number. integer variable. This parameter indicates the number of rows in the data.
	#wri_dat_mod=write data mode. string parameter. This parameter indicates the type of writting that will be perform.
def Wri_Dat_Str_Txt(txt_fil_nam,wri_dat_val,wri_dat_col_num,wri_dat_lin_num,wri_dat_mod):
	txt_fil=open(file=txt_fil_nam,mode=wri_dat_mod) #txt_fil=text file.
	for i_wri_dat_lin_num in range(0,wri_dat_lin_num,1): #i_wri_dat_lin_num=i-counter write data lines number. 
		line=''
		#print(i_wri_dat_lin_num)
		for i_wri_dat_col_num in range(0,wri_dat_col_num,1): #i_wri_dat_col_num=i-counter write data columns number.
			#print(i_wri_dat_col_num)
			line=line+wri_dat_val[i_wri_dat_lin_num][i_wri_dat_col_num]+'\t'
		line=line+'\n'
		txt_fil.write(line)
	txt_fil.close()
	return

#Wri_WYD_Mix_Txt=Write Wavelength Y Data Mixed Text.
	#This function will write the data given in a text file.
#Parameters.
	#txt_fil_nam=text file name. String parameter. This parameter indicates the directory and name of the file to be read.
	#wri_dat_val=write data values. Float array of [wri_dat_col_num][wri_dat_lin_num] dimentions. This parameter has all the data to write.
	#wri_dat_pfi=write data precision figures. Integer array of [wri_dat_col_num] dimentions. This parameter indicates the number of significative figures to be saved.
	#wri_dat_pty=write data precision type. String array of [wri_dat_col_num] dimentions. This parameter indicates the type of formating for the signifivative figures to be saved. "G" for normal and "E" for scientific formating.
	#wri_dat_col_num=write data columns number. Integer variable. This parameter indicates the number of columns in the data.
	#wri_dat_lin_num=write data lines number. Integer variable. This parameter indicates the number of rows in the data.
	#wri_dat_mod=write data mode. String parameter. This parameter indicates the type of writting that will be perform.
def Wri_WYD_Mix_Txt(txt_fil_nam,wri_dat_val,wri_dat_pfi,wri_dat_pty,wri_dat_col_num,wri_dat_lin_num,wri_dat_mod):
	txt_fil=open(file=txt_fil_nam,mode=wri_dat_mod) #txt_fil=text file.
	#print(wri_dat_col_num,wri_dat_lin_num)
	for i_wri_dat_lin_num in range(0,wri_dat_lin_num,1): #i_wri_dat_lin_num=i-counter write data lines number. 
		line=''
		for i_wri_dat_col_num in range(0,wri_dat_col_num,1): #i_wri_dat_col_num=i-counter write data columns number.
			#pre="%."+str(wri_dat_pfi[i_wri_dat_col_num])+wri_dat_pty[i_wri_dat_col_num] #pre=precision.
			#print(i_wri_dat_col_num,i_wri_dat_lin_num,wri_dat_val[i_wri_dat_col_num][i_wri_dat_lin_num])
			line=line+str(wri_dat_val[i_wri_dat_col_num][i_wri_dat_lin_num])+'\t'
		line=line+'\n'
		txt_fil.write(line)
	txt_fil.close()
	return

#Wri_WYD_Flt_Txt=Write Wavelength Y Data Float Text.
	#This function will write the data given in a text file.
#Parameters.
	#txt_fil_nam=text file name. String parameter. This parameter indicates the directory and name of the file to be read.
	#wri_dat_val=write data values. Float array of [wri_dat_col_num][wri_dat_lin_num] dimentions. This parameter has all the data to write.
	#wri_dat_pfi=write data precision figures. Integer array of [wri_dat_col_num] dimentions. This parameter indicates the number of significative figures to be saved.
	#wri_dat_pty=write data precision type. String array of [wri_dat_col_num] dimentions. This parameter indicates the type of formating for the signifivative figures to be saved. "G" for normal and "E" for scientific formating.
	#wri_dat_col_num=write data columns number. Integer variable. This parameter indicates the number of columns in the data.
	#wri_dat_lin_num=write data lines number. Integer variable. This parameter indicates the number of rows in the data.
	#wri_dat_mod=write data mode. String parameter. This parameter indicates the type of writting that will be perform.
def Wri_WYD_Flt_Txt(txt_fil_nam,wri_dat_val,wri_dat_pfi,wri_dat_pty,wri_dat_col_num,wri_dat_lin_num,wri_dat_mod):
	txt_fil=open(file=txt_fil_nam,mode=wri_dat_mod) #txt_fil=text file.
	for i_wri_dat_lin_num in range(0,wri_dat_lin_num,1): #i_wri_dat_lin_num=i-counter write data lines number. 
		line=''
		for i_wri_dat_col_num in range(0,wri_dat_col_num,1): #i_wri_dat_col_num=i-counter write data columns number.
			pre="%."+str(wri_dat_pfi[i_wri_dat_col_num])+wri_dat_pty[i_wri_dat_col_num] #pre=precision.
			line=line+str(pre%wri_dat_val[i_wri_dat_col_num][i_wri_dat_lin_num])+'\t'
		line=line+'\n'
		txt_fil.write(line)
	txt_fil.close()
	return

#Spe_Cap_Sav=Spectrum Captured Saving.
	#This function will save the capturated spectrum.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
def Spe_Cap_Sav(his_fil,spe_cap,pix_cap,dir_cap,set_cap,lab_cap):
	spe_fsa=dir_cap+'Set_'+str(set_cap)+'_'+lab_cap+'.'+mod_ipr.Dat_SIn_Typ #spe_fsa=spectrum file saved. 
	Wri_Dat_Str_Txt(spe_fsa,mod_ipr.Dat_SIn_CHe,2,2,'w')		
	Wri_WYD_Flt_Txt(spe_fsa,spe_cap,mod_ipr.Dat_SIn_CFi,mod_ipr.Dat_SIn_CFo,2,pix_cap,'a')
	return

#Spe_Cap_Sav=Spectrum Captured Saving.
	#This function will save the control variables.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#cnt_cap=control capturate. String and Float list of [5] dimention. This parameter indicates the captured set, azimutal, elevation, outside and inside temperatures at the moment of spectrum capture.
def Con_Sav(his_fil,cnt_fil,cnt_cap):
	Wri_WYD_Mix_Txt(cnt_fil,cnt_cap,mod_ipr.Dat_Cnt_CFi,mod_ipr.Dat_Cnt_CFo,6,1,'a')
	return

#Spe_Cap_Sav=Spectrum Captured Saving.
	#This function will save the control variables.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#cnt_cap=control capturate. String and Float list of [5] dimention. This parameter indicates the captured set, azimutal, elevation, outside and inside temperatures at the moment of spectrum capture.
def Fit_OD_Sav(od_fil,fit_wav_n,fit_wav,fit_od,dat_acs,fit_acs):
	od_hu=[]
	od_dat=zeros(shape=(7+2*mod_ipr.Fit_Gas_Num,fit_wav_n),dtype=float)
	for mfsffr in range(7):
		od_hu.append([])
		od_hu[mfsffr].append(mod_ipr.Dat_FOD_CHe[mfsffr][0])
		od_hu[mfsffr].append(mod_ipr.Dat_FOD_CHe[mfsffr][1])
	for i_gas in range(mod_ipr.Fit_Gas_Num):
		for ij in range(2):
			od_hu.append([])
			od_hu[7+2*i_gas+ij].append(mod_ipr.Dat_FOD_CHe[7+ij][0]+mod_ipr.Fit_Gas_Lab[i_gas])
			od_hu[7+2*i_gas+ij].append(mod_ipr.Dat_FOD_CHe[7+ij][1])	
	for wav_n in range(fit_wav_n):
		od_dat[0][wav_n]=fit_wav[wav_n]
		for mfsffr in range(6):		
			od_dat[1+mfsffr][wav_n]=fit_od[mfsffr][wav_n]
		for i_gas in range(mod_ipr.Fit_Gas_Num): 
			od_dat[7+2*i_gas][wav_n]=dat_acs[i_gas][wav_n]
			od_dat[8+2*i_gas][wav_n]=fit_acs[i_gas][wav_n]
	Wri_WYD_Mix_Txt(od_fil,od_hu,mod_ipr.Dat_Cnt_CFi,mod_ipr.Dat_Cnt_CFo,mod_ipr.Fit_Gas_Num*2+7,2,'w')
	Wri_WYD_Mix_Txt(od_fil,od_dat,mod_ipr.Dat_Cnt_CFi,mod_ipr.Dat_Cnt_CFo,mod_ipr.Fit_Gas_Num*2+7,fit_wav_n,'a')
	return

#Spe_Cap_Sav=Spectrum Captured Saving.
	#This function will save the control variables.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#cnt_cap=control capturate. String and Float list of [5] dimention. This parameter indicates the captured set, azimutal, elevation, outside and inside temperatures at the moment of spectrum capture.
def Fit_SCD_Sav(scd_fil,mea_tim,scd_fit):
	scd_line=[]
	scd_line.append([mea_tim[0]])
	for i_gas in range(mod_ipr.Fit_Gas_Num): 
		for iijjkk in range(6): 
			scd_line.append([scd_fit[i_gas][iijjkk]])
	#print(scd_fit.shape)
	#print(scd_fit)
	#print(scd_line)
	Wri_WYD_Mix_Txt(scd_fil,scd_line,mod_ipr.Dat_Cnt_CFi,mod_ipr.Dat_Cnt_CFo,mod_ipr.Fit_Gas_Num*6+1,1,'a')
	return
	
#Spe_Cap_Sav=Spectrum Captured Saving.
	#This function will save the control variables.
#Parameters.
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#cnt_fil=control file. String parameter. This parameter indicates the path to find the control file.
	#cnt_cap=control capturate. String and Float list of [5] dimention. This parameter indicates the captured set, azimutal, elevation, outside and inside temperatures at the moment of spectrum capture.
def Fit_Con_Sav(con_fil,mea_tim,con_fit):
	con_line=[]
	con_line.append(mea_tim[0])
	for i_gas in range(mod_ipr.Fit_Gas_Num): 
		for iijjkk in range(6): 
			con_line.append(scd_fit[i_gas][iijjkk])
	Wri_WYD_Mix_Txt(con_fil,con_line,mod_ipr.Dat_Cnt_CFi,mod_ipr.Dat_Cnt_CFo,mod_ipr.Fit_Gas_Num*2+1,1,'a')
	return
