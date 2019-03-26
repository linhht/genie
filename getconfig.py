#Import neccessary libraries/modules
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

#Define getconfig() function
def getconfig(device):
    device.connect()                                        #Connect to device
    output_pre = device.parse('show running-config')        #Parse 'show run' cmd & store to outout_pre structure object
    with open('config/running-config_' + str(device.name) + '.txt', 'wb') as f:
        pickle.dump(output_pre, f)                          #Write outout_pre structure object to txt file use pickle
    f.close()
    device.disconnect()                                     #Disconnect from device
    sys.exit()                                              #Exist program
