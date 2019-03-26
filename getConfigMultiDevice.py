#! python3
# getConfigMultiDevice.py - get config of devices & write to file/files.
# getConfigMultiDevice.py usage:
# python getConfigMultiDevice.py - get config of multiple devices from my_testbed.yaml file
# my_testbed.yaml file should be in current working directory
# remember to creat 'config' folder before running script

#Import neccessary libraries/modules
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

#define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

#Define getconfig() function
def getconfig(dev):
    device = genie_testbed.devices[str(dev)]                #Get device from genie_testbed var
    device.connect()                                        #Connect to device
    output_pre = device.parse('show running-config')        #Parse 'show run' cmd & store to outout_pre structure object
    with open('config/running-config_' + str(device.name) + '.txt', 'wb') as f:
        pickle.dump(output_pre, f)                          #Write outout_pre structure object to txt file use pickle
    f.close()
    device.disconnect()                                     #Disconnect from device
    
#Main program
if len(sys.argv) > 1:                                       #If user do enter more than one argument
        print('You do not need to input the argument')
        print('Usage: python getConfigMultiDevice.py')
        sys.exit()
print('Get config of multiple devices from my_testbed.yaml file'+'\n')
for dev in genie_testbed.devices.keys():
        print('Get config of ' + str(dev) + '\n')
        logfile.write('Get config of ' + str(dev) + '\n')
        try:
                getconfig(dev)
                logfile.write('Get config of ' + str(dev) + '---DONE!!!' + '\n')
        except:
                print('Failed to establish connection to ' + str(dev) + '\n')
                logfile.write('Failed to establish connection to ' + str(dev) + '\n')
                continue
logfile.close()
sys.exit()
