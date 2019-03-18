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

############################## Basic check ###############################
