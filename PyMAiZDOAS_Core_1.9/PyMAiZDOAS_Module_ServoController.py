import PyMAiZDOAS_Module_Initial_Parameters as mod_ipr #mod_ipr=module intial parameters.
from PyMAiZDOAS_Module_Register import His_Upt
from PyMAiZDOAS_Module_Read_Write import Rep_Fil_Txt

		
from RPi. GPIO import setwarnings,setmode,setup,output,cleanup,BOARD,OUT,HIGH,LOW
from os.path import exists
from sys import exit
from numpy import zeros
from time import sleep
from serial import Serial

class Srv_Ini:

	#Pico_Send=(Reaspberry) Pico Send
	def Pico_Send(self,pi3_cmd_send):
		pi3_cmd_bytes=str.encode(pi3_cmd_send)
		self.pico_usb.write(pi3_cmd_bytes)	
		return
		
	#Pico_Read=(Reaspberry) Pico Read
	def Pico_Read(self):
		pico_cmd_bytes=self.pico_usb.read(9)
		pico_cmd_read=pico_cmd_bytes.decode("ascii")
		return pico_cmd_read

	#srv_azi_ang_to_pul=servo azimutal angle to pulse
	def srv_azi_ang_to_pul(self,azi_num,azi_ang):
		azi_pul=zeros(shape=(azi_num),dtype=int,order='F')
		for ang_pul in range(azi_num):
		    azi_pul[ang_pul]=int(self.srv_azi_m*azi_ang[ang_pul]+self.srv_azi_b)
		return azi_pul

	#srv_ele_ang_to_pul=servo elevation angle to pulse
	def srv_ele_ang_to_pul(self,ele_num,ele_ang):
		ele_pul=zeros(shape=(ele_num),dtype=int,order='F')
		for ang_pul in range(ele_num):
			ang_srv=90-ele_ang[ang_pul]
			ele_pul[ang_pul]=int(self.srv_ele_m*ang_srv+self.srv_ele_b)
		return ele_pul

	#srv_mir_ang_to_pul=servo mirror angle to pulse
	def srv_mir_ang_to_pul(self,mir_num,mir_ang):
		mir_pul=zeros(shape=(mir_num),dtype=int,order='F')
		for ang_pul in range(mir_num):
			ang_srv=90-mir_ang[ang_pul]/2
			mir_pul[ang_pul]=int(self.srv_mir_m*ang_srv+self.srv_mir_b)
		return mir_pul	

	#srv_mir_ang_to_pul=servo mirror angle to pulse
	def srv_aem_ang_to_pul(self,azi_ang,ele_ang):
		self.srv_aem_pul[0]=self.srv_azi_ang_to_pul(1,[azi_ang])
		self.srv_aem_pul[1]=self.srv_ele_ang_to_pul(1,[ele_ang])
		self.srv_aem_pul[2]=self.srv_mir_ang_to_pul(1,[ele_ang])
		return

	def Pico_Reset(self):
		setmode(BOARD) #Use pin numbers (not GPIO numbers!)
		setwarnings(False)
		setup(mod_ipr.Srv_Rpb_3b_ofp,OUT) #Using pin 3 (= GPIO 2) for data output
		output(mod_ipr.Srv_Rpb_3b_ofp,HIGH)
		sleep(4)
		output(mod_ipr.Srv_Rpb_3b_ofp,LOW)
		sleep(6)
		return
		
	def Pico_Off(self):
		cleanup()
		return
		
	def Pico_Ini(self,his_fil):
		self.srv_dev_mth=True
		His_Upt(his_fil,1,'Search compleated. The servo command port was found in '+self.srv_dev_fnd)
		His_Upt(his_fil,1,'Configuration of servo object started.')
		self.srv_azi_pul=self.srv_azi_ang_to_pul(mod_ipr.Azi_Ang_Num,mod_ipr.Azi_Ang_Val)
		self.srv_ele_pul=self.srv_ele_ang_to_pul(mod_ipr.Ele_Ang_Num,mod_ipr.Ele_Ang_Val)
		self.srv_mir_pul=self.srv_mir_ang_to_pul(mod_ipr.Ele_Ang_Num,mod_ipr.Ele_Ang_Val)
		srv_ele_or=self.srv_ele_ang_to_pul(2,[mod_ipr.Srv_Ele_Ang_Off_Len,mod_ipr.Srv_Ele_Ang_Ref])
		srv_mir_or=self.srv_mir_ang_to_pul(2,[mod_ipr.Srv_Ele_Ang_Off_Mir,mod_ipr.Srv_Ele_Ang_Ref])
		self.srv_ele_act=self.srv_ele_ang_to_pul(1,[mod_ipr.Srv_Ele_0])
		self.srv_ele_act=self.srv_ele_act[0]
		self.srv_ofs_pul[0]=srv_ele_or[0]
		self.srv_ofs_pul[1]=srv_mir_or[0]
		self.srv_ref_pul[0]=srv_ele_or[1]
		self.srv_ref_pul[1]=srv_mir_or[1]
		self.pico_usb=Serial(self.srv_dev_fnd,mod_ipr.Srv_Pico_Frq)
		pi3_cmd="C"+"\t"+str(mod_ipr.Srv_Azi_Pin)+"\t"+str(mod_ipr.Srv_Ele_Pin)+"\t"+str(mod_ipr.Srv_Mir_Pin)
		pi3_cmd+="\t"+str(mod_ipr.Srv_Azi_Frq)+"\t"+str(mod_ipr.Srv_Ele_Frq)+"\t"+str(mod_ipr.Srv_Mir_Frq)
		pi3_cmd+="\t"+str(mod_ipr.Srv_Wai_Tim)+"\n"
		self.Pico_Send(pi3_cmd)
		pico_cmd=self.Pico_Read()
		His_Upt(his_fil,2,pico_cmd)
		His_Upt(his_fil,1,'Configuration of servo object complete!')
		return

	#Initialization of the class Servo Initialization.
	#This function will found all USB servo controller devices conected to the computer.
	#Parameters.
		#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	def __init__(self,his_fil):
		His_Upt(his_fil,0,'*****Checking Servo-Motors devices*****')
		His_Upt(his_fil,1,'Searching for the servo command port in the range '+mod_ipr.Srv_Cmd_Prt+str(0)+' - '+mod_ipr.Srv_Cmd_Prt+str(mod_ipr.Srv_Sea_Ran)+' ...')
		self.Pico_Reset()
		self.srv_dev_mth=False #srv_dev_mth=servo device match.
		self.srv_dev_fnd=None #srv_dev_fnd=servo device founded.
		self.srv_azi_m=mod_ipr.Srv_Azi_m #srv_azi_m=servo azimutal m (slope). float variable. Units in radians/grades.
		self.srv_azi_b=mod_ipr.Srv_Azi_b #srv_azi_b=servo azimutal b (intercep). float variable. Units in radians.
		self.srv_ele_m=mod_ipr.Srv_Ele_m #srv_ele_m=servo elevation m (slope). float variable. Units in radians/grades.
		self.srv_ele_b=mod_ipr.Srv_Ele_b #srv_ele_b=servo elevation b (intercep). float variable. Units in radians.
		self.srv_mir_m=mod_ipr.Srv_Mir_m #srv_mir_m=servo mirror m (slope). float variable. Units in radians/grades.
		self.srv_mir_b=mod_ipr.Srv_Mir_b #srv_mir_b=servo mirror b (intercep). float variable. Units in radians.
		self.srv_azi_pul=zeros(shape=(mod_ipr.Azi_Ang_Num),dtype=int,order='F') #srv_azi=servo azimutal pulses.
		self.srv_ele_pul=zeros(shape=(mod_ipr.Ele_Ang_Num),dtype=int,order='F') #srv_ele=servo elevation pulses.
		self.srv_mir_pul=zeros(shape=(mod_ipr.Ele_Ang_Num),dtype=int,order='F') #srv_mir=servo mirror pulses.
		self.srv_ofs_pul=zeros(shape=(2),dtype=int,order='F') #srv_ele=servo elevation pulses.
		self.srv_ref_pul=zeros(shape=(2),dtype=int,order='F') #srv_ele=servo elevation pulses.
		self.srv_aem_pul=zeros(shape=(3),dtype=int,order='F')
		self.srv_ele_act=0 #srv_ele_act=servo elevation actual.
		self.srv_pico_usb=None #srv_pico_usb=servo pico usb.
		self.Pico_Reset()
		for i_tst_rng in range(0,mod_ipr.Srv_Sea_Ran,1): #i_tst_rng=i-counter test range.
			self.srv_dev_fnd=mod_ipr.Srv_Cmd_Prt+str(i_tst_rng)
			if exists(mod_ipr.Srv_Cmd_Prt+str(i_tst_rng))==True:
				self.Pico_Ini(his_fil)
				break
		if self.srv_dev_mth==False: 
			His_Upt(his_fil,1,'Search compleated. Error, the servo command port was not found in the range provided. Increase the search range or check servo controller conection. Measurements collection will be stopped.')
			exit('Error. The servo command port was not found in the range provided. Increase the search range or check servo controller conection.')

	def SrvSetOff(self,his_fil):
		if self.srv_ofs_pul[0]<self.srv_ele_act: self.Pico_Send("B"+"\n")
		else: self.Pico_Send("F"+"\n")
		pico_cmd=self.Pico_Read()
		self.Pico_Send(str(self.srv_azi_pul[0])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_ofs_pul[0])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_ofs_pul[1])+"\n") 
		pico_cmd+="\t"+self.Pico_Read()
		His_Upt(his_fil,2,pico_cmd)
		self.srv_ele_act=self.srv_ofs_pul[0]
		return
		
	def SrvSetRef(self,his_fil):
		if self.srv_ref_pul[0]<self.srv_ele_act: self.Pico_Send("B"+"\n")
		else: self.Pico_Send("F"+"\n")
		pico_cmd=self.Pico_Read()
		self.Pico_Send(str(self.srv_azi_pul[0])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_ref_pul[0])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_ref_pul[1])+"\n") 
		pico_cmd+="\t"+self.Pico_Read()
		His_Upt(his_fil,2,pico_cmd)
		self.srv_ele_act=self.srv_ref_pul[0]
		return
		
	def SrvSetRST(self,his_fil):
		if self.srv_aem_pul[0]<self.srv_ele_act: self.Pico_Send("B"+"\n")
		else: self.Pico_Send("F"+"\n")
		pico_cmd=self.Pico_Read()
		self.Pico_Send(str(self.srv_aem_pul[0])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_aem_pul[1])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_aem_pul[2])+"\n") 
		pico_cmd+="\t"+self.Pico_Read()
		His_Upt(his_fil,2,pico_cmd)
		self.srv_ele_act=self.srv_aem_pul[1]
		return

	#SrvSet=Servo Set.
	#Parameters.
		#his_fil=history file. String parameter. This parameter indicates the path to find the history file.	
	def SrvSet(self,azi_n,ele_n,mir_n,his_fil):
		if self.srv_ele_pul[ele_n]<self.srv_ele_act: self.Pico_Send("B"+"\n")
		else: self.Pico_Send("F"+"\n")
		pico_cmd=self.Pico_Read()
		self.Pico_Send(str(self.srv_azi_pul[azi_n])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_ele_pul[ele_n])+"\n")
		pico_cmd+="\t"+self.Pico_Read()
		self.Pico_Send(str(self.srv_mir_pul[mir_n])+"\n") 
		pico_cmd+="\t"+self.Pico_Read()
		self.srv_ele_act=self.srv_ele_pul[ele_n]
		His_Upt(his_fil,2,pico_cmd)

#Srv_Tar=Servo Target.
	#This function will move the servo motor to the respective target.
#Parameters
	#his_fil=history file. String parameter. This parameter indicates the path to find the history file.
	#srv_dev=servo controller. Object parameter. This parameter indicates an Controller object.
	#srv_chn=servo channel. Integer parameter. This parameter indicates the servo channel.
	#srv_tar=servo target. Integer parameter. This parameter indicates the servo target.
def Srv_Tar(his_fil,srv_dev,srv_tar):
	srv_dev.SrvSet(srv_tar[0],srv_tar[1],srv_tar[2],his_fil)
	tar_rch=False #tar_rch=target reached.
	return
