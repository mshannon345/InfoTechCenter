print("**************************************")
print("Gasoline Branch\n\n")

#Import Libraraies Here
import random

def gasLevelGauge():
    gasLevelList = ["Empty","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


print(gasLevelGauge())