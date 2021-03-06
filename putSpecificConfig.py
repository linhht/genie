#! python3
# putSpecificConfig.py - put specific config from cmd file to specific devices.
# cmd file & list of devices are in cmdRouter.csv.
# Usage:
#   putSpecificConfig.py cmdRouter.csv - put command on a device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory
# cmdRouter.csv file must exist in current working directory
# Example of cmdRouter.csv:
#  command/rustphrbtqfb-1.txt,rustphrbtqfb-1
#  command/rustphrbtqfb-2.txt,rustphrbtqfb-2

#Import neccessary libraries/modules
import pickle
import sys
import pprint
from ats.topology import loader
from genie.conf import Genie
import csv

#Define global variables
testbed = loader.load('my_testbed.yaml')              #Load testbed yaml file
genie_testbed = Genie.init(testbed)                   #Init genie testbed
logfile = open('log.txt', 'w+')                       #Open log file

#Define readCommandRouterFile() --- read csv file & return to data structure obj
def readCommandRouterFile(cmdRouterFile):
  with open(cmdRouterFile) as f:
    csvf = csv.reader(f)
    data = list(csvf)
  return data

#Define readCommandFile() --- read command txt file & return to cmd structure obj
def readCommandFile(cmdFile):
  with open(cmdFile) as f:
    cmd = f.read().splitlines()
  return cmd

#Define putCommand() --- put cmd in cmdList to device, device is read from testbed file
def putCommand(dev, cmdList):
  device = genie_testbed.devices[str(dev)]                  #Get device from genie testbed
  device.connect(learn_hostname=True)                       #Connect to device
  device.configure(cmdList)                                 #Execute config cmds on device
  device.disconnect()                                       #Disconnect from device

#Main program
###If user do not enter cmdRouter.csv
if len(sys.argv) < 2:                                       
   print('Please input the cmdRouter.csv file')
   print('Usage: python putSpecificCommand.py cmdRouter.csv') 
   sys.exit()
###If user do enter cmdRouter.csv
cmdRouterFile = sys.argv[1]                                  #Store 1st sys argument (cmdRouter.csv) to cmdRouterFile var
data = readCommandRouterFile(cmdRouterFile)                  #Read cmdRouter.csv data file
for i in range (0,len(data),1):                              #len(data) = number of rows/ devices in csv file
   cmdFile = data[i][0]                                      #cdmFile in column 0
   dev = data[i][1]                                          #dev in column 1                                            
   print('Put command on ' + str(dev) + '\n')
   logfile.write('Put command on ' + str(dev) + '\n')
   cmdList = readCommandFile(str(cmdFile))                   #Read cmdList from cmdFile
   try:
      putCommand(dev, cmdList)                               #Put cmd in cmdList to dev
      logfile.write('Put command on ' + str(dev) + '---DONE!!!' + '\n')
   except:                                                   #Exception handling in case can not connect to device
      print('Failed to establish connection to ' + str(dev) + '\n')
      logfile.write('Failed to establish connection to ' + str(dev) + '\n')
      continue
logfile.close()                                              #Close log file after finish task
sys.exit()                                                   #Exit program
