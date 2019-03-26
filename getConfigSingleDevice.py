#! python3
# getConfigSingleDevice.py - get config of a device & write to file/files.
# getConfigSingleDevice.py usage:
# python getConfigSingleDevice.py <device_hostname> - get config of a specific device, device must exist in my_testbed.yaml file
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
    print('Get config of ' + str(dev) + '\n')               #Print out the msg on terminal
    logfile.write('Get config of ' + str(dev) + '\n')       #Write msg to log file
    device = genie_testbed.devices[str(dev)]                #Get device from genie_testbed var
    device.connect()                                        #Connect to device
    output_pre = device.parse('show running-config')        #Parse 'show run' cmd & store to outout_pre structure object
    with open('config/running-config_' + str(device.name) + '.txt', 'wb') as f:
        pickle.dump(output_pre, f)                          #Write outout_pre structure object to txt file use pickle
    f.close()
    logfile.write('Get config of ' + str(dev) + '---DONE!!!' + '\n')
    logfile.close()                                         #Close log file
    device.disconnect()                                     #Disconnect from device
    sys.exit()                                              #Exist program

#Main program
if len(sys.argv) < 2:                                       #If user do not enter <device_hostname>
        print('You need to input the <device_hostname>')
        print('Usage: python getConfigSingleDevice.py <device_hostname>')
        sys.exit()
dev = ' '.join(sys.argv[1:])                                #Store sys argument to dev var
getconfig(dev)                                              #Call getconfig() function with dev as argument
