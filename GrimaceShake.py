#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome Branch starts here
timeToSleep = 2

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to havethe ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center Operation System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted up - Retina Scanned - Access Granted!\n")

#Gasoline Branch Starts here
print("**************************************\n")
print("Gasoline Branch\n")

#Function that lists Gas Stations, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
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
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listsOfGasStatinons(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listsOfGasStatinons(),"which is",milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank full.")
    else:
        print("Your gas tank is full - horrayyy!")

gasLevelAlert()

print("\n**************************************\n")

print("Weather Branch\n")

#create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowing", "blizzard", "raining", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once VRS(Vehicle Response System) is detemined
weatherAlert = weather()

def vehicaleResponseSystem():
    if weatherAlert == "snowing":
        print("\nNational Weather Service has been updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has been updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has been updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has been updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has been updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has been updated our alarm by 60 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("National Weather service forecast", weatherAlert,"weather conditions")
        sleep(1.5)
        print("VRS has been disengaged! Drive at your own risk")


vehicaleResponseSystem()
