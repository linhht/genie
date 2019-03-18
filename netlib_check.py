#! python3
# netlib_check.py - get current config of device, check & troubleshoot the state.
# Usage:
#   python netlib_check.py <device_hostname> - device must exist in my_testbed.yaml file
# 

############################## Import neccessary libraries/modules ###############################
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

############################## Define global variables ###############################
testbed = loader.load('/root/workspace/devnet-2595/workshop/genie/my_testbed.yaml') #location of testbed file
genie_testbed = Genie.init(testbed) #load testbed file to genie
logfile = open('log_netlib_check.txt', 'w+')    #open logfie
###Check input argument
if len(sys.argv) < 2:   #if there is NO hostname arg
    print('Please input the device name')
    print('Usage: python netlib_check.py <device_hostname>')
    sys.exit()    
dev = ' '.join(sys.argv[1:])    #if there is hostname, put it in 'dev' variable

############################## Define functions ###############################
def check_bgp_status():
    print('Get BGP status of ' + str(dev) + '\n')
    logfile.write('Get BGP status of ' + str(dev) + '\n')
    device = genie_testbed.devices[str(dev)]    #get device from testbed file
    device.connect()    #connect to device
    output = device.parse('show bgp all summary')   #parse command 'show bgp all summary' to 'output' variable
    ### loop thru neighbors in output & check number of received prefixes
    ### if number of received prefixes is integer --> neighbor is OK
    ### if number of received prefixes is NOT integer --> neighbor is NOK
    for k,v in output['vrf']['default']['neighbor'].items():
        if v['address_family']['ipv4 unicast']['state_pfxrcd'].isdigit():
            print('Neighbor: ' + k + 'is UP and receive ' + str(v['address_family']['ipv4 unicast']['state_pfxrcd']) + ' prefixes')
            logfile.write('Neighbor: ' + k + 'is UP and receive ' + str(v['address_family']['ipv4 unicast']['state_pfxrcd']) + ' prefixes' + '\n')
            continue
        print('Neighbor: ' + k + 'is NOK')
        logfile.write('Neighbor: ' + k + 'is NOK' + '\n')
    #logfile.close()
    #device.disconnect()
    #continue
    #sys.exit()
    
############################## Main program ###############################
while (True):
       print('\n\n##################################################')
       print('1-Check interface status')
       print('2-Check BGP status')
       print('3-Exit')
       print('##################################################\n\n')
       prompt = input('Please select from above option: ')
       if (prompt == "1"):
           print('1-Proceed Check interface status \n\n')
           #check_And_Change()
       elif (prompt == "2"):
           print('2-Check BGP status \n\n')
           check_bgp_status()
       elif (prompt == "3"):
           break
