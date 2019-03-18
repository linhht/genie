#! python3
# netlib_check.py - get current config of device, check & troubleshoot the state.
# Usage:
#   python check_config.py <device_hostname> - device must exist in my_testbed.yaml file
# 

############################## Import neccessary libraries/modules ###############################
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie

############################## Define functions ###############################
#def check_bgp_status():
    

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
