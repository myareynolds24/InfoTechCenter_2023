print("*************************************************************************")
print("Gasoline Branch\n\n")

# import libraries here
import random
from time import sleep

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