import os
import pandas as pd
import numpy as np
from scipy import interpolate
import DOAS_Fit_Plot as Plt
import DOAS_Fit_Minimize as Min

azi,ele=150,30
tim_num=100
pix_num=3648
gases_num=5
spec_win_sta=375
spec_win_end=390
fit_pol_grd=5
fit_fil_pss=5 #fit_fil_pss=fit filter pass. integer variable.
fit_fil_ord=3 #fit_fil_ord=fit filter order. integer variable.
fit_fil_cff=0.1 #fit_fil_cff=fit filter cutoff. float variable.
fit_fil_sr=12 #fit_fil_sr=fit sample rate. float variable.

mea_dir="/mnt/Data_Mount/Documents_RGI/SubGroup_DOAS/Test_MAiZ_DOAS/Data_Spectrum_Intensities_2023_10_04/"
off_fil="./Offset.txt"
ref_fil="./Reference.txt"
spec_col=["wav","int","Bad"]
acs_col=["wav","acs"]

ofs_dat=pd.read_csv(off_fil,delimiter="\t",skiprows=2,names=spec_col,header=None)
ref_dat=pd.read_csv(ref_fil,delimiter="\t",skiprows=2,names=spec_col,header=None)
wav_dat=np.zeros(shape=(pix_num),dtype=float)
spec_dat=np.zeros(shape=(3,pix_num),dtype=float)
wav_dat=ofs_dat.wav
spec_dat[0],spec_dat[1]=ofs_dat.int,ref_dat.int

spec_win_pxl_sta=0
spec_win_pxl_end=0
spec_win_pnt=0
fit_wav=[]
for pxl in range(pix_num):
    if spec_win_sta<=wav_dat[pxl]: spec_win_pxl_sta+=1
    else: break
for pxl in range(pix_num):
    if spec_win_sta<=wav_dat[pxl] and wav_dat[pxl]<=spec_win_end:
        fit_wav.append(wav_dat[pxl])
        spec_win_pnt+=1
spec_win_pxl_end=spec_win_pxl_sta+spec_win_pnt
mea_fit=np.zeros(shape=(6,spec_win_pnt),dtype=float)
fit_wav=np.array(fit_wav,dtype=float)
gases_dir="/mnt/Data_Mount/Documents_RGI/SubGroup_DOAS/Test_MAiZ_DOAS/ACS/"
gases_lab=["O4","NO2","OClO","BrO","HCHO"]
acs_dat=np.zeros(shape=(gases_num,spec_win_pnt),dtype=float)
acs_fit=np.zeros(shape=(gases_num,spec_win_pnt),dtype=float)
tim=[]
gases_scd=[]
gases_con=[]
gases_acs_int=[]
for i_gas in range(gases_num):
    i_gas_acs=pd.read_csv(gases_dir+gases_lab[i_gas]+"_gg.txt",delimiter="\t",skiprows=0,names=acs_col,header=None)
    i_gas_acs_intrpl=interpolate.interp1d(i_gas_acs.wav,i_gas_acs.acs)
    gases_acs_int.append(i_gas_acs_intrpl)
    i_gas_acs_intrpl_pnts_tmp=i_gas_acs_intrpl(fit_wav)
    acs_dat[i_gas]=i_gas_acs_intrpl_pnts_tmp
    gases_scd.append([])
    gases_con.append([])

fit_continue=True
azi,ele=int(azi),int(ele)
set_n=int(0)
plot_obj=Plt.Plot_Initialize(gases_num,gases_lab,wav_dat,spec_dat,fit_wav,mea_fit,acs_dat,acs_fit,gases_scd,gases_con,tim)
while fit_continue:
    file_name="Set_"+str(set_n)+"_Azi_"+str(azi)+"_Ele_"+str(ele)+".txt"
    file_path=mea_dir+file_name
    file_exist=os.path.isfile(file_path)
    print("Fitting for file",file_name)
    tim.append(set_n)
    if file_exist:
        data_mea=pd.read_csv(file_path,delimiter="\t",skiprows=2,names=spec_col,header=None)
        spec_dat[2]=data_mea.int
        mea_fit=Min.Prepare_Data(spec_dat,fit_wav,mea_fit,spec_win_pxl_sta,spec_win_pxl_end,spec_win_pnt,fit_pol_grd,fit_fil_ord,fit_fil_pss,fit_fil_cff,fit_fil_sr)
        gases_scd,gases_scd_ite,mea_fit,acs_fit,upd_acs=Min.Fit_SCD(gases_num,spec_win_pnt,fit_wav,mea_fit,gases_acs_int,acs_dat,acs_fit,gases_scd)
        gases_con=Min.Est_Con(gases_num,gases_scd_ite,gases_con)
        Plt.Plot_Update(plot_obj,gases_num,gases_lab,file_name,spec_dat[2],mea_fit,acs_fit,gases_scd,gases_con,tim,upd_acs)
        #input("continue?")
    else: fit_continue=False
    set_n+=1