print("\n******************\n")

print("Weather Branch\n")

#Important Libraries Here
import random
from time import sleep

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
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has been updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has been updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has been updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has been updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has been updated our alarm by 60 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("National Weather service forecast", weatherAlert,"weather condotions")
        print("VRS has been disengaged! DRive at your own risk")


vehicaleResponseSystem()