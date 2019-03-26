#! python3
# putSpecificCommand.py - put specific command/commands from cmd file to specific devices.
# cmd file & list of devices are in cmdRouter.csv.
# Usage:
#   python putSpecificCommand.py cmdRouter.csv - put command on a device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory
# cmdRouter.csv file must exist in current working directory
# Example of cmdRouter.csv:
#  rustphrbtqfb-1.txt,rustphrbtqfb-1
#  rustphrbtqfb-2.txt,rustphrbtqfb-2

#Import neccessary libraries/modules
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie
import csv

#Define global variables
testbed = loader.load('my_testbed.yaml')
genie_testbed = Genie.init(testbed)
logfile = open('log.txt', 'w+')

#Define readCommandRouterFile()
def readCommandRouterFile(cmdRouterFile):
  with open(cmdRouterFile) as f:
    csvf = csv.reader(f)
    data = list(csvf)
  return data

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
if len(sys.argv) < 2:                                       #If user do not enter cmdRouter.csv
   print('Please input the cmdRouter.csv file')
   print('Usage: python putSpecificCommand.py cmdRouter.csv') 
   sys.exit()
#If user do enter cmdRouter.csv
cmdRouterFile = sys.argv[1]                                  #Store 1st sys argument to cmdRouterFile var
data = readCommandRouterFile(cmdRouterFile)
for i in range (0,len(data),1):                              #len(data) = number of rows/ devices in csv file
   cmdFile = data[i][0]                                      #cdmFile in column 0
   dev = data[i][1]                                          #dev in column 1                                            
   print('Put command on ' + str(dev) + '\n')
   logfile.write('Put command on ' + str(dev) + '\n')
   cmdList = readCommandFile(str(cmdFile))
   try:
      putCommand(dev, cmdList)
      logfile.write('Put command on ' + str(dev) + '---DONE!!!' + '\n')
   except:
      print('Failed to establish connection to ' + str(dev) + '\n')
      logfile.write('Failed to establish connection to ' + str(dev) + '\n')
      continue
logfile.close()
sys.exit()
