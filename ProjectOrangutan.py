'''
Our Welcome Screen will start our program letting drivers know that the InfoTech Center 2023 is loading
'''
#Import Libraries Here
import sys
import time

timetosleep = 2

print("\nWelcome - InfoTech Center 2023\n")
time.sleep(timetosleep)

#Add code to have the ellipsis add a dot every .5 secs
x = 0
ellipsis = 0

while x != 20:
     x += 1
     msg = ("InfoTech Center 2023 is loading" + "." * ellipsis)
     ellipsis = ellipsis + 1
     sys.stdout.write("\r" + msg) # \r prints a carriage return first, so, message is printed on top of prevoius line
     time.sleep(.5)
     if ellipsis == 4:
          ellipsis = 0
     if x == 20:
          print("\n\nOperating System Loaded" + "\nRetina Scanned, Access Granted!")
