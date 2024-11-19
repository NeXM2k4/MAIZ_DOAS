###################################################################################
##PyMA&ZDOAS Module Initial Parameters -- Version 1.5                                ##
##The parameters on this module are used to adjust the measurements of MA&ZDOAS.##
###################################################################################

#Directories path settings.
Dir_Rea_Cro_Sec='/home/leo1/Documents/PyMAiZDOAS/PyMAiZDOAS_Data/Data_Cross_Sections/' #Dir_Rea_Cro_Sec=Directory Read Cross Sections. String parameter. No units.
Dir_Sav_Mai_Pth='/home/leo1/Documents/PyMAiZDOAS/' #Dir_Sav_Mai_Pth=Directory Save Main Path. String parameter. No units.
Dir_Sav_Spe_Int='Data_Spectrum_Intensities/' #Dir_Sav_Opt_Den=Directory Saved Optical Densities. String parameter. No units.
Dir_Sav_Ofs='Data_Offsets/' #Dir_Sav_Ofs=Directory Saved Offsets. String parameter. No units.
Dir_Sav_Ref='Data_Reference/' #Dir_Sav_Ref=Directory Saved Reference. String parameter. No units.
Dir_Sav_Fit_ODn='Data_Fit_Optical_Densities/' #Dir_Sav_Fit_ODn=Directory Saved Optical Densities. String parameter. No units.
Dir_Sav_Fit_Set='Data_Fit_Settings/' #Dir_Sav_Fit_Set=Directory Saved Fits Settings. String parameter. No units.
Dir_Sav_Fit_SCD='Data_Fit_Slant_Column_Densities/' #Dir_Sav_Fit_SCD=Directory Saved Slant Column Densities. String parameter. No units.
Dir_Sav_Fit_Con='Data_Fit_Concentrations/' #Dir_Sav_Fit_Con=Directory Saved Concentrations. String parameter. No units.

#Time settings.
Cap_Tim_Sta=[0,1,0] #Cap_Tim_Sta=Capture Time Start. Integer array of [3] dimentions. Units on [hours,minutes,seconds]. 24 hours format used.
Cap_Tim_Fin=[23,59,0] #Cap_Tim_Fin=Capture Time Finish. Integer array of [3] dimentions. Units on [hours,minutes,seconds]. 24 hours format used.
Cap_Tim_Sta_Wai_His=1 #Cap_Tim_Sta_Wai_His=Capture Time Start Waiting History. Integer parameter. Units on Hours.
Cap_Tim_Sta_Wai_Scr=60 #Cap_Tim_Sta_Wai_Scr=Capture Time Start Waiting Screen. Integer parameter. Units on seconds.
Cap_Day_Month_Year=[0,0,0] #Cap_Year_Moth_Day=Capture Year Month Day. No units. This value will self-populate do not touch it.

#Spectral window settings.
Spe_Win_Sta=390 #Spectral Window Start. Float parameter. Units of nanometers.
Spe_Win_Fin=410 #Spectral Window Finish. Float parameter. Units of nanometers.
Spe_Fit_Num=0 #Spe_Fit_Num=Spectral Number Pixels. No units. This value will self-populate do not touch it. 
#Spe_Pxl_Num=0 #Spe_Pxl_Num=Spectral Number Pixels. No units. This value will self-populate do not touch it. 

#Spectrometer settings.
Spc_Lab_Ser='USB4H06056' #'USB4C02660' #Spc_Lab=Spectrometer Label Serial. String variable. No units.
Spc_Ite_Tim=100000 #Spc_Ite_Tim=Spectrometer Integration Time. Float parameter. Units in micro-seconds.
Spc_Sca_Num=3 #Spc_Sca_Num=Spectrometer Scans Number. Integer parameter. No units.
Spc_Box_Car=0 #Spc_Box_Car=Spectrometer Box Car. Integer parameter. No units.
Spc_Pxl_Num=0 #Spc_Pxl_Num=Spectrometer Number Pixels. No units. This value will self-populate do not touch it. 

#Measurement angles settings.
Azi_Ang_Num=1 #4 #Azi_Ang_Num=Azimutal Angles Number. Integer parameter. No units.
Azi_Ang_Val=[0]#,45,90,135,180,225,270,315,360] #[90,75,60] #Azi_Ang_Val=Azimutal Angles Values. Float array of [Azi_Ang_Num] dimension. Units in Degrees.
Ele_Ang_Num=6 #Ele_Ang_Num=Elevation Angles Number. Integer parameter. No units.
Ele_Ang_Val=[0,15,30,45,60,75]#[0,15,30,45,60,75] #Ele_Ang=Elevation Angles. Float array of [Ele_Ang_Num] dimension. Units in Degrees.

#Measurement solar tracker settings.
Sol_Trk_Act=True #Sol_Trk_Act=Solar Tracking Activated. Boolean parameter. No units.
Lat_Val_Pos=13.721622475515062 #Lat_Val_Pos=Latitude Value Position. Float parameter. No units. 
Lon_Val_Pos=-89.2025175431812 #Lon_Val_Pos=Longitude Position Value. Float parameter. No units.
Tim_Zon_Pos='America/El_Salvador' #Tim_Zon_Pos=Time Zone Position. String parameter. No units. pytz timezones.
Tim_Zon_Int=0 #Tim_Zon_Int=Time Zone Integer. No units. This value will self-populate do not touch it.

#Data storage settings.
Dat_Fld_Nam="MAiZ_Measurements_" #Dat_Fld_Nam=Data Folder Measurement. String parameter. No units.
Dat_Cnt_Nam="MAiZ_Measurements_Control_" #Dat_Cnt_Nam=Data Control Name. String parameter. No units.
Dat_His_Nam="MAiZ_Measurements_History_" #Dat_His_Nam=Data History Name. String parameter. No units.
Dat_Sto_HD5=False #Dat_Sto_DH5=Data Storage Hierarchical Data file 5. Boolean parameter. No units.
Dat_Sto_Txt=True #Dat_Sto_Tex=Data Storage Text file. Boolean parameter. No units.
Dat_Sto_Spe_Win_Onl=False #Dat_Sto_Spe_Win_Onl=Data Storage Spectral Window Only. Boolean parameter. No units.
Dat_Cnt_CHe=[['Set','Azimutal','Elevation','time','Temp Outside','Temp Inside'],['No units','degrees','degrees','hours','C','C']] #Dat_Cnt_CHe=Data Control Column Headers. String array of [2][5] dimention. No units.
Dat_Cnt_CFi=[1,3,3,5,5,5] #Dat_Cnt_CFi=Data Control Column presicion Figures. Integer array of [5] dimention. No units.
Dat_Cnt_CFo=["G","G","G","G","G"] #Dat_Cnt_CFo=Data Control Column presicion Formating. String array of [5] dimention. No units.
Dat_Cnt_Typ='txt' #Dat_Cnt_Typ=Data Controln Type. String variable. Some values are: txt, csv, etc. No units. For more information read file parameter in open function.
Dat_SIn_CHe=[['Wavelength','Intensities'],['nm','a.u.']] #Dat_SIn_CHe=Data Spectrum Intensities Column Headers. String array of [2][2] dimention. No units.
Dat_SIn_CFi=[5,5] #Dat_SIn_CFi=Data Spectrum Intensities Column presicion Figures. Integer array of [2] dimention. No units.
Dat_SIn_CFo=["G","G"] #Dat_SIn_CFo=Data Spectrum Intensities Column presicion Formating. String array of [2] dimention. No units.
Dat_SIn_Typ='txt' #Dat_SIn_Typ=Data Spectrum Intensities Type. String variable. Some values are: txt, csv, etc. No units. For more information read file parameter in open function.
Dat_ACS_CHe=[['Wavelength','nm'],['Cross Section','(1/m^{2})']] #Dat_ACS_CHe=Data Absorption Cross Section Column Headers. String array of [2][2] dimention. No units.
Dat_ACS_CFi=[5,5] #Dat_ACS_CFi=Data Absorption Cross Section Column presicion Figures. Integer array of [2] dimention. No units.
Dat_ACS_CFo=["G","E"] #Dat_ACS_CFo=Data Absorption Cross Section Column presicion Formating. String array of [2] dimention. No units.
Dat_ACS_Typ='txt' #Dat_ACS_Typ=Data Absorption Cross Section Type. String variable. Some values are: txt, csv, etc. No units. For more information read file parameter in open function.
Dat_FOD_CHe=[['Wavelength','nm'],['OD','---'],['Filtered','---'],['Slow','---'],['Fast','---'],['Fit','---'],['Residual','---'],['Mea_ACS_','(mole/m^{2})'],['Fit_ACS_','(mole/m^{2})']] #Dat_FOD_CHe=Data Absorption Cross Section Column Headers. String array of [2][2] dimention. No units.
Dat_FOD_CFi=[5,5] #Dat_FOD_CFi=Data Absorption Cross Section Column presicion Figures. Integer array of [2] dimention. No units.
Dat_FOD_CFo=["G","E"] #Dat_FOD_CFo=Data Absorption Cross Section Column presicion Formating. String array of [2] dimention. No units.
Dat_FOD_Typ='txt' #Dat_FOD_Typ=Data Absorption Cross Section Type. String variable. Some values are: txt, csv, etc. No units. For more information read file parameter in open function.
Dat_SCD_CHe=[['Time','HH'],['SCD_F_','mol/m^{2}'],['SCD_E_','mol/m^{2}'],['Shift_F_','(nm)'],['Shift_E_','(nm)'],['Squezee_F_','(---)'],['Squezee_E_','(---)']] #Dat_FOD_CHe=Data Absorption Cross Section Column Headers. String array of [2][2] dimention. No units.
Dat_SCD_CFi=[5,5] #Dat_FOD_CFi=Data Absorption Cross Section Column presicion Figures. Integer array of [2] dimention. No units.
Dat_SCD_CFo=["G","E"] #Dat_FOD_CFo=Data Absorption Cross Section Column presicion Formating. String array of [2] dimention. No units.
Dat_SCD_Typ='txt' #Dat_FOD_Typ=Data Absorption Cross Section Type. String variable. Some values are: txt, csv, etc. No units. For more information read file parameter in open function.
Dat_Con_CHe=[['Time','HH'],['Con_F_','mol/m^{3}'],['Con_E_','(nm)']] #Dat_FOD_CHe=Data Absorption Cross Section Column Headers. String array of [2][2] dimention. No units.
Dat_Con_CFi=[5,5] #Dat_FOD_CFi=Data Absorption Cross Section Column presicion Figures. Integer array of [2] dimention. No units.
Dat_Con_CFo=["G","E"] #Dat_FOD_CFo=Data Absorption Cross Section Column presicion Formating. String array of [2] dimention. No units.
Dat_Con_Typ='txt' #Dat_FOD_Typ=Data Absorption Cross Section Type. String variable. Some values are: txt, csv, etc. No units. For more information read file parameter in open function.

#Servo-motor settings.
Srv_Ele_0=0
Srv_Cmd_Prt='/dev/ttyACM' #Srv_Cmd_Prt=Servo Command Port. String variable. No units.
Srv_Rpb_3b_ofp=3 #Srv_Rpb_3b_ofp=Servo Raspberry 3b+ on off pico. Integer variable. No units.
Srv_Rpb_Pico_Ser="2e8a:0005" #Srv_Rpb_Pico_Ser=Servo Raspberry Pico Serial. String variable. No units. 
Srv_Pico_Frq=115200 #Srv_Pico_Frq=Servo (Raspberry) Pico Frecuency. String variable. Units in hz.
Srv_Sea_Ran=9 #Srv_Sea_Ran=Servo Search Range. Integer variable. No units.
Srv_Wai_Tim=3 #Srv_Wai_Tim=Servo Waiting Time. Float parameter. Units in seconds.
Srv_Azi_Pin=2 #Srv_Azi_Pin=Servo Azimutal Pinout. Integer variable. No units.
Srv_Ele_Pin=3 #Srv_Ele_Pin=Servo Elevation Pinout. Integer variable. No units.
Srv_Mir_Pin=4 #Srv_Mir_Pin=Servo Mirror Pinout. Integer variable. No units.
Srv_Azi_Frq=50 #Srv_Azi_Frq=Servo Azimutal Frecuency. Integer variable. Units in Mhz.
Srv_Ele_Frq=50 #Srv_Ele_Frq=Servo Elevation Frecuency. Integer variable. Units in Mhz.
Srv_Mir_Frq=50 #Srv_Mir_Frq=Servo Mirror Frecuency. Integer variable. Units in Mhz.
Srv_Azi_m=0.0065500e6  #+0.0135000e6 #0.0135714 #srv_azi_m=servo azimutal m (slope). float variable. Units in radians/grades.
Srv_Azi_b=0.5000000e6 #srv_azi_b=servo azimutal b (intercep). float variable. Units in radians.
Srv_Ele_m=+0.01050e6 #0.0120000e6 #0116667 #srv_ele_m=servo elevation m (slope). float variable. Units in radians/grades.
Srv_Ele_b=+0.620000e6 #+0.6000000e6 #srv_ele_b=servo elevation b (intercep). float variable. Units in radians.
Srv_Mir_m=-0.01050e6 #-0.0144000e6 #-0.0144440e6 # #srv_mir_m=servo mirror m (slope). float variable. Units in radians/grades.
Srv_Mir_b=+2.05000e6 #+2.5000000e6 #+2.6000000e6 # #srv_mir_b=servo mirror b (intercep). float variable. Units in radians.
Srv_Ele_Ang_Off_Len=0 #Srv_Ele_Ang_Off=Servo Elevation Angle Offset. Float variable. Units in degrees.
Srv_Ele_Ang_Off_Mir=45 #Srv_Ele_Ang_Off=Servo Elevation Angle Offset. Float variable. Units in degrees.
Srv_Ele_Ang_Ref=90 #Srv_Ele_Ang_Ref=Servo Elevation Angle Reference. Float variable. Units in degrees.

#Measureament processing settings.
Fit_SCD=True #Fit_SCD=Fit Slant Column Densities. Boolean parameter. No units.
Fit_Con=False #Fit_Con=Fit Concentrations. Boolean parameter. No units.
Fit_Pol_Gra=4 #Fit_Pol_Gra=Fit Polynomial Grade. Integer parameter. No units.
Fil_Pss=5
Fil_ORD=3
Fil_CFF=0.1
Fil_SR=12
Fit_Gas_Num=3 #Fit_Gas_Num=Fit Gases Number. Integer parameter. No units.
Fit_Gas_Lab=['O4','HCHO','NO2','OClO','BrO'] #Fit_Gas_Lab=Fit Gases Label. String array of [Fit_Gas_Num] dimension. No units.
Fit_Gas_ACS_Fil=['O4_gg.txt','HCHO_gg.txt','NO2_gg.txt','OClO_gg.txt','BrO_gg.txt'] #Fit_Gas_Abs_Cro_Sec_Fil=Fit Gases Absorption Cross Section Files. Array of [Fit_Gas_Num] dimension. No units.

#Plot settings.
Plt_Itn_Sav=False #Plt_Itn_Sav=Plot Intensities Saving. Boolean parameter. No Units.
Plt_Itn_Shw=True #Plt_Itn_Shw=Plot Intensities Showing. Boolean parameter. No Units.
Plt_Itn_Tit='Absorption Cross Section (ACS) used' #Plt_Itn_Tit=Plot Intensities Title. String parameter. No Units.
Plt_Itn_LRI=['Reference ACS','Interpolated ACS'] #Plt_Itn_LRI=Plot Intensities Label Reference Interpolation. String parameter. No units.
Plt_Itn_Lwd=[1.0,1.0] #Plt_Itn_Lwd=Plot Intensities Linewidth. Float parameter. No units. For more information read linewidth parameter in matplotlib.pyplot.plot function.
Plt_Itn_Mar=[',','o'] #Plt_Itn_Mar=Plot Intensities Markers. String parameter. No units. For more information read marker parameter in matplotlib.pyplot.plot function.
Plt_Itn_CRI=['red','blue'] #Plt_Itn_CRI=Plot Intensities Color Reference Interpolation. String parameter. No units. For more information read color parameter in matplotlib.pyplot.plot function.
Plt_Itn_Axs=['Wavelength (nm)','Optical Density'] #Plt_Itn_Axs=Plot Intensities Axis. String array of [2] dimention. No units. For more information read matplotlib.pyplot.xlabel and matplotlib.pyplot.xlabel functions.
Plt_Itn_LgP=1 #Plt_Itn_LgP=Plot Intensities Legend Position. Integer or string parameter. Values range form 0-8. It can also be string combination of upper, lower, middle, right, left and center. No units. For more information read about matplotlib.pyplot.title function.
Plt_Itn_Siz='a4' #Plt_Itn_Siz=Plot Intensities Size. String variable. Values in range form a0-a10. No units. For more information read papertype parameter in matplotlib.pyplot.savefig function.
Plt_Itn_BBx='tight' #Plt_Itn_BBx=Plot Intensities b box. String variable. Values are None and tight. No units. For more information read bbox_inches parameter in matplotlib.pyplot.savefig function.
Plt_Itn_Typ='png' #Plt_Itn_Typ=Plot Intensities Type. String variable. Some values are: png, pdf, jpg, eps, etc. No units. For more information read format parameter in matplotlib.pyplot.savefig function.
Plt_OMS_Sav=False #Plt_OMS_Sav=Plot Optical Density Measured Simulated Saving. Boolean parameter. No Units.
Plt_OMS_Shw=True #Plt_OMS_Shw=Plot Optical Density Measured Simulated Showing. Boolean parameter. No Units.
Plt_OMS_Tit='Optical Density for measurement' #Plt_OMS_Tit=Plot Optical Density Measured Simulated Title. String parameter. No Units.
Plt_OMS_LRI=['Measured OD','Simulated OD'] #Plt_OMS_LRI=Plot Optical Density Measured Simulated Label Reference Interpolation. String parameter. No units.
Plt_OMS_Lwd=[1.0,1.0] #Plt_OMS_Lwd=Plot Optical Density Measured Simulated Linewidth. Float parameter. No units. For more information read linewidth parameter in matplotlib.pyplot.plot function.
Plt_OMS_Mar=['o','o'] #Plt_OMS_Mar=Plot Optical Density Measured Simulated Markers. String array of [2] dimentions. No units. For more information read marker parameter in matplotlib.pyplot.plot function.
Plt_OMS_CRI=['red','blue'] #Plt_OMS_CRI=Plot Optical Density Measured Simulated Color Reference Interpolation. String array of [2] dimentions. No units. For more information read color parameter in matplotlib.pyplot.plot function.
Plt_OMS_Axs=['Wavelength (nm)','Optical Density'] #Plt_OMS_Axs=Plot Optical Density Measured Simulated Axis. String array of [2] dimention. No units. For more information read matplotlib.pyplot.xlabel and matplotlib.pyplot.xlabel functions.
Plt_OMS_LgP=1 #Plt_OMS_LgP=Plot Optical Density Measured Simulated Legend Position. Integer or string parameter. Values range form 0-8. It can also be string combination of upper, lower, middle, right, left and center. No units. For more information read about matplotlib.pyplot.title function.
Plt_OMS_Siz='a4' #Plt_OMS_Siz=Plot Optical Density Measured Simulated Size. String variable. Values in range form a0-a10. No units. For more information read papertype parameter in matplotlib.pyplot.savefig function.
Plt_OMS_BBx='tight' #Plt_OMS_BBx=Plot Optical Density Measured Simulated b box. String variable. Values are None and tight. No units. For more information read bbox_inches parameter in matplotlib.pyplot.savefig function.
Plt_OMS_Typ='png' #Plt_OMS_Typ=Plot Optical Density Measured Simulated Type. String variable. Some values are: png, pdf, jpg, eps, etc. No units. For more information read format parameter in matplotlib.pyplot.savefig function.
Plt_ACS_Sav=False #Plt_ACS_Sav=Plot Absorption Cross Section Saving. Boolean parameter. No Units.
Plt_ACS_Shw=False #Plt_ACS_Shw=Plot Absorption Cross Section Showing. Boolean parameter. No Units.
Plt_ACS_Tit='Absorption_Cross_Section' #Plt_ACS_Tit=Plot Absorption Cross Section Title. String parameter. No Units.
Plt_ACS_LRI=['Reference ACS','Interpolated ACS'] #Plt_ACS_LRI=Plot Absorption Cross Section Label Reference Interpolation. String parameter. No units.
Plt_ACS_Lwd=[1.0,1.0] #Plt_ACS_Lwd=Plot Absorption Cross Section Linewidth. Float parameter. No units. For more information read linewidth parameter in matplotlib.pyplot.plot function.
Plt_ACS_Mar=['.',',','o','+','*','x'] #Plt_ACS_Mar=Plot Absorption Cross Section Markers. String array of [Azi_Ang_Num+1] dimention. No units. For more information read marker parameter in matplotlib.pyplot.plot function.
Plt_ACS_CRI=['magenta','red','blue','black','orange','green'] #Plt_ACS_CRI=Plot Absorption Cross Section Color Reference Interpolation. String array of [Ele_Ang_Num+1] dimention. No units. For more information read color parameter in matplotlib.pyplot.plot function.
Plt_ACS_Axs=['Wavelength (nm)','Cross Section (1/m^{2})'] #Plt_ACS_Axs=Plot Absorption Cross Section Axis. String array of [2] dimention. No units. For more information read matplotlib.pyplot.xlabel and matplotlib.pyplot.xlabel functions.
Plt_ACS_LgP=1 #Plt_ACS_LgP=Plot Absorption Cross Section Legend Position. Integer or string parameter. Values range form 0-8. It can also be string combination of upper, lower, middle, right, left and center. No units. For more information read about matplotlib.pyplot.title function.
Plt_ACS_Siz='a4' #Plt_ACS_Siz=Plot Absorption Cross Section Size. String variable. Values in range form a0-a10. No units. For more information read papertype parameter in matplotlib.pyplot.savefig function.
Plt_ACS_BBx='tight' #Plt_ACS_BBx=Plot Absorption Cross Section b box. String variable. Values are None and tight. No units. For more information read bbox_inches parameter in matplotlib.pyplot.savefig function.
Plt_ACS_Typ='png' #Plt_ACS_Typ=Plot Absorption Cross Section Type. String variable. Some values are: png, pdf, jpg, eps, etc. No units. For more information read format parameter in matplotlib.pyplot.savefig function.
Plt_SCD_Sav=True #Plt_SCD_Sav=Plot Slant Column Densities Saving. Boolean parameter. No Units.
Plt_SCD_Shw=False #Plt_SCD_Shw=Plot Slant Column Densities Showing. Boolean parameter. No Units.
Plt_SCD_Tit='Slant Column Densities' #Plt_SCD_Tit=Plot Slant Column Densities Title. String parameter. No Units.
Plt_SCD_LRI=['Reference ACS','Interpolated ACS'] #Plt_SCD_LRI=Plot Slant Column Densities Label Reference Interpolation. String parameter. No units.
Plt_SCD_Lwd=1.0 #Plt_SCD_Lwd=Plot Slant Column Densities Linewidth. Float parameter. No units. For more information read linewidth parameter in matplotlib.pyplot.plot function.
Plt_SCD_Mar=['.',',','o','+','*','x'] #Plt_SCD_Mar=Plot Slant Column Densities Markers. String array of [Azi_Ang_Num] dimention. No units. For more information read marker parameter in matplotlib.pyplot.plot function.
Plt_SCD_CRI=['red','blue','black','orange','green'] #Plt_SCD_CRI=Plot Slant Column Densities Color Reference Interpolation. String array of [Ele_Ang_Num] dimention. No units. For more information read color parameter in matplotlib.pyplot.plot function.
Plt_SCD_Axs=['Time (Hours)','Molecules*meters^(-1) (1/m)'] #Plt_SCD_Axs=Plot Slant Column Densities Axis. String array of [2] dimention. No units. For more information read matplotlib.pyplot.xlabel and matplotlib.pyplot.xlabel functions.
Plt_SCD_LgP=1 #Plt_SCD_LgP=Plot Slant Column Densities Legend Position. Integer or string parameter. Values range form 0-8. It can also be string combination of upper, lower, middle, right, left and center. No units. For more information read about matplotlib.pyplot.title function.
Plt_SCD_Siz='a4' #Plt_SCD_Siz=Plot Slant Column Densities Size. String variable. Values in range form a0-a10. No units. For more information read papertype parameter in matplotlib.pyplot.savefig function.
Plt_SCD_BBx='tight' #Plt_SCD_BBx=Plot Slant Column Densities b box. String variable. Values are None and tight. No units. For more information read bbox_inches parameter in matplotlib.pyplot.savefig function.
Plt_SCD_Typ='png' #Plt_SCD_Typ=Plot Slant Column Densities Type. String variable. Some values are: png, pdf, jpg, eps, etc. No units. For more information read format parameter in matplotlib.pyplot.savefig function.
Plt_Con_Sav=False #Plt_Con_Sav=Plot Concentrations Saving. Boolean parameter. No Units.
Plt_Con_Shw=True #Plt_Con_Shw=Plot Concentrations Showing. Boolean parameter. No Units.
Plt_Con_Tit='Concentrations' #Plt_Con_Tit=Plot Concentrations Title. String parameter. No Units.
Plt_Con_LRI=['Reference ACS','Interpolated ACS'] #Plt_Con_LRI=Plot Concentrations Label Reference Interpolation. String parameter. No units.
Plt_Con_Lwd=1.0 #Plt_Con_Lwd=Plot Concentrations Linewidth. Float parameter. No units. For more information read linewidth parameter in matplotlib.pyplot.plot function.
Plt_Con_Mar=['.',',','o','+','*','x'] #Plt_Con_Mar=Plot Concentrations Markers. String array of [Azi_Ang_Num] dimention. No units. For more information read marker parameter in matplotlib.pyplot.plot function.
Plt_Con_CRI=['red','blue','black','orange','green'] #Plt_Con_CRI=Plot Concentrations Color Reference Interpolation. String array of [Ele_Ang_Num] dimention. No units. For more information read color parameter in matplotlib.pyplot.plot function.
Plt_Con_Axs=['Time (hours)','Molecules*meters^(-3) (m^(-3))'] #Plt_Con_Axs=Plot Concentrations Axis. String array of [2] dimention. No units. For more information read matplotlib.pyplot.xlabel and matplotlib.pyplot.xlabel functions.
Plt_Con_LgP=1 #Plt_Con_LgP=Plot Concentrations Legend Position. Integer or string parameter. Values range form 0-8. It can also be string combination of upper, lower, middle, right, left and center. No units. For more information read about matplotlib.pyplot.title function.
Plt_Con_Siz='a4' #Plt_Con_Siz=Plot Concentrations Size. String variable. Values in range form a0-a10. No units. For more information read papertype parameter in matplotlib.pyplot.savefig function.
Plt_Con_BBx='tight' #Plt_Con_BBx=Plot Concentrations b box. String variable. Values are None and tight. No units. For more information read bbox_inches parameter in matplotlib.pyplot.savefig function.
Plt_Con_Typ='png' #Plt_Con_Typ=Plot Concentrations Type. String variable. Some values are: png, pdf, jpg, eps, etc. No units. For more information read format parameter in matplotlib.pyplot.savefig function.

#Test settings.
Slp_Tim=2 #Slp_Tim=Sleep time. Float parameter. Units in seconds.
Spc_Dev_Fnd=True #Spc_Dev_Fnd=Spectrometer Device Found. Boolean parameter. No units.
Spc_Pix_Sta=100 #Spc_Pix_Sta=Spectrometer Pixel Start. Float variable. No units.
Spc_Pix_Fin=999 #Spc_Pix_Fin=Spectrometer Pixel Finish. Float variable. No units.
Spc_Pix_Num=3000 #Spc_Pix_Num=Spectrometer Pixel Number. Integer variable. No units.
Spc_Ite_Tim_Min=10 #Spc_Ite_Tim_Min=Spectrometer Integration Time Minimum. Float parameter. Units in micro-seconds.
Spc_Ite_Tim_Max=100000000 #Spc_Ite_Tim_Max=Spectrometer Integration Time Maximum. Float parameter. Units in micro-seconds.
Spc_Noi_Lvl=5 #Spc_Noi_Lvl=Spectrometer Noise Level. Float variable. No units.
Srv_Dev_Azi_Fnd=True #Srv_Dev_Azi_Fnd=Servo Device Azimutal Found. Boolean parameter. No units.
Srv_Dev_Ele_Fnd=True #Srv_Dev_Ele_Fnd=Servo Device Elevation Found. Boolean parameter. No units.
Srv_Dev_Azi_Acc_Min=1 #Srv_Dev_Azi_Acc_Min=Servo Device Azimutal Acceleration Minimum. Integer parameter. No units.
Srv_Dev_Azi_Acc_Max=255 #Srv_Dev_Azi_Acc_Max=Servo Device Azimutal Acceleration Maximum. Integer parameter. No units.
Srv_Dev_Azi_Vel_Min=1 #Srv_Dev_Azi_Vel_Min=Servo Device Azimutal Velocity Minimum. Integer parameter. No units.
Srv_Dev_Azi_Vel_Max=255 #Srv_Dev_Azi_Vel_Max=Servo Device Azimutal Velocity Maximum. Integer parameter. No units.
Srv_Dev_Azi_Pul_Min=1000 #Srv_Dev_Azi_Pul_Min=Servo Device Azimutal Pulse Minimum. Integer parameter. Units in micro-seconds.
Srv_Dev_Azi_Pul_Max=10000 #Srv_Dev_Azi_Pul_Max=Servo Device Azimutal Pulse Maximum. Integer parameter. Units in micro-seconds.
Gas_SCD=[1.0*10**15,6.7*10**16,3.5*10**14] #Gas_SCD=Gases Slant Column Densities. Float variable. molecules*meter^(-2).


