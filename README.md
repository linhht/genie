# getConfig.py - get config of device/devices & write to file/files.
# getConfig.py usage:
# python getConfig.py - get config of multiple devices from my_testbed.yaml file
# python getConfig.py <device_hostname> - get config of a specific device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working folder
# remember to creat 'config' folder before running script

================================================================================================================================
# checkConfig.py - get current config of device & compare to pre-stored config.
# checkConfig.py usage:
# python checkConfig.py <device_hostname> - get & compare config of a specific device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory
# pre-stored config must be collected & put to 'config' directory first

================================================================================================================================
# putCommand.py - put command/commands from cmd.txt to device/ multiple devces.
# Usage:
#   python putCommand.py cmd.txt <device_hostname> - put command on a device, device must exist in my_testbed.yaml file
#   python putCommand.py cmd.txt - put command on multiple devices in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory

================================================================================================================================
# putSpecificCommand.py - put specific command/commands from cmd file to specific devices.
# cmd file & list of devices are in cmdRouter.csv.
# Usage:
#   python putSpecificCommand.py cmdRouter.csv - put command on a device, device must exist in my_testbed.yaml file
# my_testbed.yaml file must exist in current working directory
# cmdRouter.csv file must exist in current working directory
# Example of cmdRouter.csv:
#  command/rustphrbtqfb-1.txt,rustphrbtqfb-1
#  command/rustphrbtqfb-2.txt,rustphrbtqfb-2
