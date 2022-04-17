import requests
from bs4 import BeautifulSoup
import random

def getWeather(town):
    result = requests.get(town)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    temp = soup.find(class_="TodayDetailsCard--feelsLikeTempValue--Cf9Sl").text
    return temp[0:-1]

def betterWeather(townA, townB):
    weatherA = int(getWeather(townA))
    weatherB = int(getWeather(townB))
    #copmare weather
    if weatherA >= weatherB:
        return townA
    elif weatherB >= weatherA:
        return townB
    #if weather is the same for both towns
    randWeather = random.randint(0,1)
    if randWeather == 0:
        return townA
    return townB
