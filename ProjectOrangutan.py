print("\n*********************************************\n")
print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function randomly chooses the weather from the list
def weather():
    weatherForecast = ["Sunny","Cloudy","Snowing","a Blizzard","Rainy","Stormy","Icy","Foggy","Windy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
weather()

# print("The today it is " + weatherCondition)