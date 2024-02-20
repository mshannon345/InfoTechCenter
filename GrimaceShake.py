print("**************************************")
print("Gasoline Branch\n\n")

#Import Libraraies Here
import random
from time import sleep

#Function that lists Gas Stations, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listsOfGasStatinons():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Mobile","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***Warning - YOU ARE EMPTY***\n")
        sleep(2.5)
        print("  ***Calling Triple AAA***")


gasLevelAlert()
