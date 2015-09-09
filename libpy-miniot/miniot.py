'''
MinIoT, A Simple GPIO Python Framework for OpenWRT
Written by Okyza Maherdy Prabowo
Email: okyzaprabowo@live.com
'''

import os
import sys
import commands

def pinMode(direction, pin_number):
    if (direction == "output"):
        command1 = "echo %s > /sys/class/gpio/export" % pin_number 
        os.system(command1)
        command2 = "echo out > /sys/class/gpio/gpio%s/direction" % pin_number
        os.system(command2)
    elif (direction == "input"):
        command1 = "echo %s > /sys/class/gpio/export" % pin_number 
        os.system(command1)
        command2 = "echo in > /sys/class/gpio/gpio%s/direction" % pin_number
        os.system(command2)
    elif (direction == "clear"):
        command1 = "echo 0 > /sys/devices/virtual/gpio/gpio%s/value" % pin_number 
        os.system(command1)
        command2 = "echo %s > /sys/class/gpio/unexport" % pin_number
        os.system(command2)
    else:
        print "wrong direction or pin_number"
        
def writePin(value, pin_number):
    command1 = "echo %d > /sys/devices/virtual/gpio/gpio%s/value" % (value, pin_number)
    os.system(command1)

def readPin(pin_number):
    command = "cat /sys/class/gpio/gpio%s/value" % pin_number
    return commands.getoutput(command)