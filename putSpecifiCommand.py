Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@linhht Sign out
1
0 0 linhht/genie
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
genie/putCommand.py
@linhht linhht Update putCommand.py
ba2731c 9 minutes ago
61 lines (55 sloc)  2.24 KB
    
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
  device.disconnect()

#Main program
if len(sys.argv) < 3:                                       #If user do not enter <device_hostname>
    print('Put command on multiple devices from my_testbed.yaml file'+'\n')
    cmdFile = sys.argv[1]
    cmdList = readCommandFile(str(cmdFile))
    for dev in genie_testbed.devices.keys():
        print('Put command on ' + str(dev) + '\n')
        logfile.write('Put command on ' + str(dev) + '\n')
        try:
                putCommand(dev, cmdList)
                logfile.write('Put command on ' + str(dev) + '---DONE!!!' + '\n')
        except:
                print('Failed to establish connection to ' + str(dev) + '\n')
                logfile.write('Failed to establish connection to ' + str(dev) + '\n')
                continue
    logfile.close()
    sys.exit()
#If user do not enter <device_hostname> -- len(sys.argv) = 3, start from 0, end at 2
cmdFile = sys.argv[1]                                        #Store 1st sys argument to cmdFile var
dev = sys.argv[2]                                            #Store 2nd sys argument to dev var
print('Put command on ' + str(dev) + '\n')
logfile.write('Put command on ' + str(dev) + '\n')
cmdList = readCommandFile(str(cmdFile))
putCommand(dev, cmdList)
logfile.write('Put command on ' + str(dev) + '---DONE!!!' + '\n')
logfile.close()
sys.exit()
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
