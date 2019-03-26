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
    print('Get config of ' + str(dev) + '\n')
    logfile.write('Get config of ' + str(dev) + '\n')
    device = genie_testbed.devices[str(dev)]
    device.connect()
    output_pre = device.parse('show running-config')
    with open('config/running-config_' + str(device.name) + '.txt', 'wb') as f:
        pickle.dump(output_pre, f)
    f.close()
    logfile.write('Get config of ' + str(dev) + '---DONE!!!' + '\n')
    logfile.close()
    device.disconnect()
    sys.exit()

#Main program
if len(sys.argv) < 2:
        print('You need to input the <device_hostname>')
        print('Usage python getConfigSingleDevice.py <device_hostname>')
        sys.exit()
dev = ' '.join(sys.argv[1:])
getconfig(dev)
