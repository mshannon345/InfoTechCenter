print("\n***********************************************\n")

print("Weather Branch\n")

#Important Libraries Here
import random
from time import sleep

#create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowing","Blizzards","Raining", "Foggy", "Windy", "Icy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions


print(weather())