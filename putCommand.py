#! python3
# putCommand.py - put command/commands from cmd.txt to device/ multiple devces.
# Usage:
#   python putCommand.py cmd.txt <device_hostname> - put command on a device, device must exist in my_testbed.yaml file
#   python putCommand.py cmd.txt - put command on multiple devices in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory

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

#Main program
dev = ' '.join(sys.argv[1:])                                #Store sys argument to dev var
print('Put command on ' + str(dev) + '\n')
logfile.write('Put command on ' + str(dev) + '\n')
device = genie_testbed.devices[str(dev)]
device.connect()
device.execute('sh ip int bri')
device.disconnect()
logfile.write('Put command on ' + str(dev) + '---DONE!!!' + '\n')
logfile.close()
sys.exit()
