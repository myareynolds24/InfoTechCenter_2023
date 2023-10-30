print("*************************************************************************")
print("Gasoline Branch\n\n")

# import libraries here
import random
from time import sleep

# Function that lists gas stations, randomly choosing one, anf Returning it's value
def gaslevelguage():
    gasLevelList = ["EMPTY","LOW","QUARTER TANK","HALF TANK","THREE-SLAYING-QUARTER TANK","FULL TANK"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function will call the gaslevelguage to determine gas level and then find a close gas station if low
def gaslevelalert():
    mlsToGasStationLow = round(random.uniform(1, 25), 1)
    mlsToGasStationQtr = round(random.uniform(25.1, 50), 1)
