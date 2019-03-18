#! python3
# get_config.py - get config of device/devices & write to file/files.
# get_config.py usage:
# python get_config.py - get config of multiple devices from my_testbed.yaml file
# python get_config.py <device_hostname> - get config of a specific device, device must exist in my_testbed.yaml file

############################## Import neccessary libraries/modules ###############################
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

#define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

# python get_config.py - get config of multiple devices from my_testbed.yaml file
if len(sys.argv) < 2:
    print('Get config of multiple devices from my_testbed.yaml file')
    for device in genie_testbed.devices.values():
        print('Get config of ' + str(device) + '\n')
        logfile.write('Get config of ' + str(device) + '\n')
        try:
            device.connect()
            output_pre = device.parse('show running-config')
            with open('config/running-config_' + str(device.name) + '.txt', 'wb') as f:
                pickle.dump(output_pre, f)
            f.close()
            logfile.write('Get config of ' + str(device) + '---DONE!!!' + ''\n')
            device.disconnect()
        except:
            print('Failed to establish connection to ' + str(device) + '\n')
            logfile.write('Failed to establish connection to ' + str(device) + '\n')
            continue
    logfile.close()
    sys.exit()
# python get_config.py <device_hostname> - get config of a specific device, device must exist in my_testbed.yaml file
dev = ' '.join(sys.argv[1:])
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
