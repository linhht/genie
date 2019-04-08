#! python3
# getConfig.py - get config of device/devices & write to file/files.
# getConfig.py usage:
# python getConfig.py - get config of multiple devices from my_testbed.yaml file
# python getConfig.py <device_hostname> - get config of a specific device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working folder
# remember to creat 'config' folder before running script

#Import neccessary libraries/modules
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

#Define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

#Define getconfig() function
def getconfig(dev):
    device = genie_testbed.devices[str(dev)]                #Get device from genie_testbed var
    device.connect(learn_hostname=True)                                        #Connect to device
    output_pre = device.parse('show running-config')        #Parse 'show run' cmd & store to outout_pre structure object
    with open('config/running-config_' + str(device.name) + '.txt', 'wb') as f:
        pickle.dump(output_pre, f)                          #Write outout_pre structure object to txt file use pickle
    f.close()
    device.disconnect()                                     #Disconnect from device
    
#Main program
if len(sys.argv) < 2:                                       #If user do not enter <device_hostname>
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
dev = ' '.join(sys.argv[1:])                                #Store sys argument to dev var
print('Get config of ' + str(dev) + '\n')
logfile.write('Get config of ' + str(dev) + '\n')
getconfig(dev)                                              #Call getconfig() function with dev as argument
logfile.write('Get config of ' + str(dev) + '---DONE!!!' + '\n')
logfile.close()
sys.exit()

