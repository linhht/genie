#! python3
# checkConfig.py - get current config of device & compare to pre-stored config.
# checkConfig.py usage:
# python checkConfig.py <device_hostname> - get & compare config of a specific device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory
# pre-stored config must be collected & put to 'config' directory first

############################## Import neccessary libraries/modules ###############################
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

#define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log_check.txt', 'w+')

# python check_config.py <device_hostname> - get & compare config of a specific device, device must exist in my_testbed.yaml file
if len(sys.argv) < 2:
    print('Please input the device name')
    print('Usage: python check_config.py <device_hostname>')
    sys.exit()
dev = ' '.join(sys.argv[1:])
print('Get config of ' + str(dev) + '\n')
logfile.write('Get config of ' + str(dev) + '\n')
device = genie_testbed.devices[str(dev)]
device.connect(learn_hostname=True)
output_post = device.parse('show running-config')
with open('config/running-config_' + str(device.name) + '.txt', 'rb') as f:
    output_pre = pickle.load(f)
from genie.utils.diff import Diff
diff = Diff(output_pre, output_post)
diff.findDiff()
print(diff)
logfile.write('Difference of ' + str(dev) + '\n')
logfile.write(str(diff) + '\n')
f.close()
logfile.close()
device.disconnect()
sys.exit()
