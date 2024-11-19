from numpy import zeros
from pysolar.solar import get_altitude,get_azimuth
import datetime
from pytz import timezone
from matplotlib.pyplot import title,subplot,plot,xlabel,ylabel,savefig,show

lat=13.676946 #lat=latitude.
lon=-89.301659 #longitud.
Tim_Zon_Pos='America/El_Salvador'
tim_sta=[5,0,0]
tim_end=[18,0,0]

azi_val=zeros(shape=((tim_end[0]-tim_sta[0])*60),dtype=float,order='F')
ele_val=zeros(shape=((tim_end[0]-tim_sta[0])*60),dtype=float,order='F')
tim_val=zeros(shape=((tim_end[0]-tim_sta[0])*60),dtype=float,order='F')

print('Starting calculating angles...')
loc_zon=timezone(Tim_Zon_Pos)
t_i=0 #t_i=time index.
for t_h in range(tim_sta[0],tim_end[0],1):
	for t_m in range(0,59,1):
		tim_val[t_i]=t_h+t_m/60
		print('\t'+'calculation for time',tim_val[t_i],'started...')
		date=datetime.datetime(2020,6,14,t_h,t_m,0,0,tzinfo=loc_zon)
		azi_val[t_i]=get_azimuth(lat,lon,date)
		ele_val[t_i]=get_altitude(lat,lon,date)
		t_i=t_i+1

title('Azimutal and elevation angles for sun tracking')

subplot(2,1,1)
plot(tim_val,azi_val,'o-')
xlabel('time (s)')
ylabel('Azimutal values')

subplot(2,1,2)
plot(tim_val,ele_val,'.-')
xlabel('time (s)')
ylabel('Elevation values')

savefig("./Azimutal_and_Elevation_PySolar.png")
show()


