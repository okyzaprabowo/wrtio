'''
Blink Example
written by Okyza Maherdy Prabowo
Email: okyzaprabowo@live.com
'''

from miniot import *
from time import sleep

pinMode("output",21)

try:
    while True:
        writePin(1,21)
        sleep(1)
        writePin(0,21)
        sleep(1)
except KeyboardInterrupt:
    pinMode("clear",21)
    print "Thank you from MinIoT"