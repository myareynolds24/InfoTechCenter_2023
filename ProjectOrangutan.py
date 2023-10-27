print("*************************************************************************")
print("Gasoline Branch\n\n")

# import libraries here
import random
from time import sleep

def gaslevelguage():
    gasLevelList = ["EMPTY","LOW","QUARTER TANK","HALF TANK","THREE-SLAYING-QUARTER TANK","FULL TANK"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel
