'''
Our Welcome Screen will start our program letting drivers know that the InfoTech Center 2023 is loading
'''
#Import Libraries Here
import sys
import time
import random
from time import sleep

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

print("*************************************************************************")
print("Checking Current Gas Levels\n")
sleep(1)
# Function that lists gas stations, randomly choosing one, anf Returning it's value
def gasLevelGuage():
    gasLevelList = ["EMPTY","LOW","QUARTER TANK","HALF TANK","THREE-SLAYING-QUARTERS TANK","FULL TANK"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of gas stations
def listOfGasStations():
    gasStations = ["Shell","Speedway","Exxon","Meijer","Costco","Marathon","BP","Circle K","Wesco"]
    gasSationsNear = random.choice(gasStations)
    return gasSationsNear

# Function will call the gaslevelguage to determine gas level and then find a close gas station if low
def gasLevelAlert():
    mlsToGasStationLow = round(random.uniform(1, 25), 1)
    mlsToGasStationQtr = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGuage()
    if gasLevelIndicator == "EMPTY":
        print("WARNING - you are on empty")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "LOW":
        print("You gas tank is very low, checking Google Maps for the nearest gas station.")
        sleep(1.5)
        print("the closest gas station is ",listOfGasStations," which is ",mlsToGasStationLow," miles away.")
    elif gasLevelIndicator == "QUARTER TANK":
        print("You have a quarter tank of gas, checking Google Maps for the nearest gas station.")
        sleep(1.5)
        print("The closest gas station is ",listOfGasStations()," which is ",mlsToGasStationQtr," miles away.")
    elif gasLevelIndicator == "HALF TANK":
        print("You have a half tank of gas, enjoy your ride.")
    elif gasLevelIndicator == "THREE-SLAYING-QUARTERS TANK":
        print("Your gas is at Three Quarters.")
    else:
        print("Your gas is full.")
gasLevelAlert()

print("\n*********************************************\n")
print("Weather Branch\n")

#Create a function randomly chooses the weather from the list
def weather():
    weatherForecast = ["Sunny","Cloudy","Snowing","a Blizzard","Rain","Icy Roads","Fog","Wind"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
# Variable to call weather() once in our Vehicle Response System - AKA: VRS
# VRS function will allow my vehicle to respond based on weather conditions
weatherAlert = weather()

def VRS():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forecast of " + weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 50 mph, sorry for the massive inconvenience")
    elif weatherAlert == "a Blizzard":
        print("\nNational Weather Service hates you and has updated your alarm by 45 minutes because of the forecast of " + weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 30 mph, sorry for causing you road rage!")
    elif weatherAlert == "Rain":
        print("\nNational Weather Service has updated your alarm by 10 minutes because of the forecast of " + weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 60 mph :)")
    elif weatherAlert == "Fog":
        print("\nNational Weather Service really hates you and has updated your alarm by 25 minutes because of the forecast of " + weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 45 mph, wish you got that extra sleep right?")
    elif weatherAlert == "Wind":
        print("\nNational Weather Service has updated your alarm by a whole 5 minutes because of the forecast of " + weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 65 mph... did you finish your dream?")
    elif weatherAlert == "Icy Roads":
        print("\nNational Weather Service hates you and has updated your alarm by a whole 60 minutes because of the forecast of " + weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 25 mph, I advise you to stay home and watch movies instead. Call in and say your sick 😉")
    elif weatherAlert == "Sunny":
        print("\nThe weather forcast is calling for a " + weatherAlert + " day. Enjoy your drive to work!")
    else:
        print("\nThe weather forcast is calling for a " + weatherAlert + " day.")
VRS()

