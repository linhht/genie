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
from getConfigSingleDevice import getconfig

#define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

#Main program
if len(sys.argv) > 1:                                       #If user do enter more than one argument
        print('You do not need to input the argument')
        print('Usage: python python getConfigMultiDevice.py')
        sys.exit()
print('Get config of multiple devices from my_testbed.yaml file')
for device in genie_testbed.devices.values():
    print('Get config of ' + str(device) + '\n')
    logfile.write('Get config of ' + str(device) + '\n')
    try:
        getconfig(device)
    except:
        print('Failed to establish connection to ' + str(device) + '\n')
        logfile.write('Failed to establish connection to ' + str(device) + '\n')
        continue
logfile.close()
sys.exit()

