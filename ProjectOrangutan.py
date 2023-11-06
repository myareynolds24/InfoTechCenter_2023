print("\n*********************************************\n")
print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

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