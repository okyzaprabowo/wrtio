'''
Digital Input Example using LED and Button
Developed by Okyza Maherdy Prabowo
Email: okyzaprabowo@live.com
'''
from miniot import *

try:
    pinMode("output",22)
    pinMode("input",21)
    while True:
        value = readPin(21)
        if (value == '1'):
            writePin(1,22)
        else:
            writePin(0,22)

except KeyboardInterrupt:
    pinMode("clear",21)
    pinMode("clear",22)
    print "Thank you from MinIoT"