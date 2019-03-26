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
import getconfig

#Define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

#Main program
if len(sys.argv) < 2:                                       #If user do not enter <device_hostname>
        print('You need to input the <device_hostname>')
        print('Usage: python getConfigSingleDevice.py <device_hostname>')
        sys.exit()
dev = ' '.join(sys.argv[1:])                                #Store sys argument to dev var
print('Get config of ' + str(dev) + '\n')               #Print out the msg on terminal
logfile.write('Get config of ' + str(dev) + '\n')       #Write msg to log file
device = genie_testbed.devices[str(dev)]                #Get device from genie_testbed var
getconfig()                                              #Call getconfig()
logfile.write('Get config of ' + str(dev) + '---DONE!!!' + '\n')
logfile.close()                                         #Close log file
