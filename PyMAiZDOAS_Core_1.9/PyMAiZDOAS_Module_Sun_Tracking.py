import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
from PyMAiZDOAS_Module_Register import Tim_Upt_Int

from numpy import zeros
from pysolar.solar import get_altitude,get_azimuth
from datetime import datetime

#srv_dev_use=spectrometer device used. Object <Spectrometer> parameter. This parameter is an object for the USB spectrometer configuration.
def Solar_Position(srv_dev_use):
	tim_act=Tim_Upt_Int()
	date=datetime(mod_ipr.Cap_Day_Month_Year[2],mod_ipr.Cap_Day_Month_Year[1],mod_ipr.Cap_Day_Month_Year[0],int(tim_act[0]),int(tim_act[1]),int(tim_act[2]),0,tzinfo=mod_ipr.Tim_Zon_Int)
	azi_val=get_azimuth(mod_ipr.Lat_Val_Pos,mod_ipr.Lon_Val_Pos,date)
	ele_val=get_altitude(mod_ipr.Lat_Val_Pos,mod_ipr.Lon_Val_Pos,date)
	srv_dev_use.srv_aem_ang_to_pul(azi_val,ele_val)
	return azi_val,ele_val
