import matplotlib.pyplot as plt
import numpy as np
import PyMAiZDOAS_Module_Read_Write as mod_raw #mod_raw=module read and write.

direc='/home/leo1/Documents/PyMAiZDOAS/PyMAiZDOAS_Data/Data_Cross_Section/'
gas_fil='BrO_gg.txt'
# Data for plotting
gas_acs_ref=mod_raw.Rea_Fil_Txt_Flt(direc+gas_fil) #gas_acs_ref=gas absorption cros sections reference. gas_acs_ref[0]==wavelenght. gas_acs_ref[1]==acs. 
#print(gas_acs_ref[0])


fig, ax = plt.subplots()
ax.plot(gas_acs_ref[0],gas_acs_ref[1])

ax.set(xlabel='wavelenght (nm)', ylabel='ACS',title=gas_fil)
ax.grid()

fig.savefig("test.png")
plt.show()

