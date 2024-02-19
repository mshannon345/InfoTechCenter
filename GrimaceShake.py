print("**************************************")
print("Gasoline Branch\n\n")

#Import Libraraies Here
import random

#Function that lists Gas Stations, randomly chppson one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listsOfGasStatinons():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Mobile","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby


print(gasLevelGauge())
print(listsOfGasStatinons())