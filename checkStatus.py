#! python3
# checkStatus.py - check status of a device.
# Usage:
#   python checkStatus.py <device_hostname> - device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory

#Import neccessary libraries/modules
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie
import time

#Define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

#Define readCommandFile()
def readCommandFile(cmdFile):
  with open(cmdFile) as f:
    cmd = f.read().splitlines()
  return cmd
  
#Define putCommand()
def putCommand(dev, cmdList):
  device = genie_testbed.devices[str(dev)]
  device.connect()
  for cmd in cmdList:
    device.execute(str(cmd))
    time.sleep(3)
  #device.disconnect()

#Main program
while (True):
       print('\n\n##################################################')
       print('1-Check overal status: interface, dmvpn, BGP, ip route, PFR, Waas')
       print('2-Check BGP status')
       print('2-Check BGP status')
       print('2-Check BGP status')
       print('2-Check BGP status')
       print('2-Check BGP status')
       print('2-Check BGP status')
       print('2-Check BGP status')
       print('9-Exit')
       print('##################################################\n\n')
       prompt = input('Please select from above option: ')
       if (prompt == "1"):
           print('1-Check overal status: interface, dmvpn, BGP, ip route, PFR, Waas \n\n')
           cmdList = readCommandFile('cmdOveral.txt')
           dev = sys.argv[1]
           putCommand(dev, cmdList)
       elif (prompt == "2"):
           print('2-Check BGP status \n\n')
           #check_bgp_status()
       elif (prompt == "9"):
           break
