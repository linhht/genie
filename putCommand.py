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
cmdFile = ' '.join(sys.argv[1:])                            #Store 1st sys argument to cmdFile var
dev = ' '.join(sys.argv[2:])                                #Store 2nd sys argument to dev var
print('Put command on ' + str(dev) + '\n')
logfile.write('Put command on ' + str(dev) + '\n')
cmdList = readCommandFile(str(cmdFile))
putCommand(dev, cmdList)
logfile.write('Put command on ' + str(dev) + '---DONE!!!' + '\n')
logfile.close()
sys.exit()
