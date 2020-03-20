## Imports
import discord
from discord.ext import commands, tasks
import sys
from os import system, listdir, getcwd
from random import randint, randrange
from termcolor import colored as cld
import requests
from datetime import datetime

## Pre-Main
def cls():
    system("cls")

def pause(mode=0):
    if mode == 0:
        system("pause")
    elif mode == 1:
        system("pause>nul")
    else:
        print("Nope.")

def getFmtTime(mode=0):
    if mode == 0:
        now = datetime.now()
        timeStamp = now.strftime("%H:%M:%S")
        fullTimeStamp = "[" + timeStamp + "]"
        return fullTimeStamp
    else:
        print("Not supported at this time.")
        return "Nope."

def getFmtDate(mode=0):
    if mode == 0:
        now = datetime.now()
        dateStamp = now.strftime("%Y/%m/%d")
        fullDateStamp = "[" + dateStamp + "]"
        return fullDateStamp
    else:
        print("Not supported at this time.")
        return "Nope."

def setTitle(title):
    system(f"title {title}")

def qExit():
    SystemExit()

## Main(s)
def menu():
    cls()
    print(cld("[RHQOnline]", "green"), cld("Welcome to RHQOnline's nCov / Coronavirus / COVID19 Tracker Application."))
    print(cld("[RHQOnline]", "green"), cld("To begin using the application, please input the name of a country..."))
    print("")

    basicDataFetch = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    parse = basicDataFetch.json()

    cases = parse['cases']
    deaths = parse['deaths']
    recoveries = parse['recovered']
    deaths_to_recovered = (deaths/recoveries)*100

    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Current Confirmed Cases       :   {:,}".format(cases)))
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Current Confirmed Deaths      :   {:,}".format(deaths)))
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Current Confirmed Recoveries  :   {:,}\n".format(recoveries)))
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Death-to-Recovery Ratio       :   %s%%" % format("%.2f" % deaths_to_recovered)))
    print("")
    countryToFind = str(input("~search@: "))
    print("")
    searchForCountry(countryToFind)

def searchForCountry(country):
    isAltName = checkForExceptions(country)
    if isAltName == True:
        uaeStrings = ['united arab emirates', 'arab emirates', 'united arab', 'emirates', 'unitedarabemirates', 'the uae']
        ukStrings = ['scotland', 'united kingdom', 'unitedkingdom', 'the uk']
        usStrings = ['america', 'united states', 'united states of america', 'the us', 'the usa']
        countryName = country
        if country.lower() in uaeStrings:
            countryName = "uae"
        elif country.lower() in ukStrings:
            countryName = "uk"
        elif country.lower() in usStrings:
            countryName = "usa"
        urlToQuery = requests.get("https://coronavirus-19-api.herokuapp.com/countries/%s" % countryName)
        data = urlToQuery.json()
        country = data['country']
        cases = data['cases']
        tdCases = data['todayCases']
        deaths = data['deaths']
        tdDeaths = data['todayDeaths']
        recovered = data['recovered']
        active = data['active']
        critical = data['critical']
        casesPOM = data['casesPerOneMillion']
        displaySearchResults(country, cases, deaths, recovered, active, critical, casesPOM, tdCases, tdDeaths)
    elif isAltName == False:
        urlToQuery = requests.get("https://coronavirus-19-api.herokuapp.com/countries/%s" % country)
        data = urlToQuery.json()
        country = data['country']
        cases = data['cases']
        tdCases = data['todayCases']
        deaths = data['deaths']
        tdDeaths = data['todayDeaths']
        recovered = data['recovered']
        active = data['active']
        critical = data['critical']
        casesPOM = data['casesPerOneMillion']
        displaySearchResults(country, cases, deaths, recovered, active, critical, casesPOM, tdCases, tdDeaths)

def displaySearchResults(country, cases, deaths, recovered, active, critical, casesPOM, tdCases, tdDeaths):
    cls()
    print(cld("[RHQOnline]", "green"), cld("The results displayed below are detailed statistics."))
    print(cld("[RHQOnline]", "green"), cld("The results are updated hourly."))
    print(cld("[RHQOnline]", "green"), cld("You are fetching this dataset at %s on %s.\n\n" % (getFmtTime(), getFmtDate())))

    deaths_to_recovered = (deaths/recovered)*100

    print(cld("[DATA]", "green"), cld("Country in Question         :   %s" % country))
    print(cld("[DATA]", "green"), cld("----------------------------------------------"))
    print(cld("[DATA]", "green"), cld("Total Confirmed Cases       :   {:,}".format(cases)))
    print(cld("[DATA]", "green"), cld("Total Cases Today           :   {:,}".format(tdCases)))
    print(cld("[DATA]", "green"), cld("Total Confirmed Deaths      :   {:,}".format(deaths)))
    print(cld("[DATA]", "green"), cld("Total Deaths Today          :   {:,}".format(tdDeaths)))
    print(cld("[DATA]", "green"), cld("Total Confirmed Recoveries  :   {:,}".format(recovered)))
    print(cld("[DATA]", "green"), cld("----------------------------------------------"))
    print(cld("[DATA]", "green"), cld("Total Active Cases          :   {:,}".format(active)))
    print(cld("[DATA]", "green"), cld("Total in Critical Condition :   {:,}".format(critical)))
    print(cld("[DATA]", "green"), cld("Cases per One Million       :   {:,}".format(casesPOM)))

    print(cld("\n\n[RHQOnline]", "green"), cld("Press any key to try again, or 'CTRL+C' to exit..."))
    pause(0)
    menu()

def checkForExceptions(country):
    uaeStrings = ['united arab emirates', 'arab emirates', 'united arab', 'emirates', 'unitedarabemirates', 'the uae']
    ukStrings = ['scotland', 'united kingdom', 'unitedkingdom', 'the uk']
    usStrings = ['america', 'united states', 'united states of america']

    if country.lower() in uaeStrings:
        return True
    if country.lower() in ukStrings:
        return True
    if country.lower() in usStrings:
        return True
    else:
        return False

## Script
setTitle("RHQOnline's nCov COVID19 Tracker")
try:
    menu()
except KeyboardInterrupt:
    print(cld("\n\n" + getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[ERROR]", "red"), cld("Manual Hault Detected. Exiting..."))
    pause(0)
    qExit()
except:
    print(cld("\n" + getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[ERROR]", "red"), cld("Invalid country entered. Please try again.")) # f"{getFmtDate()} {getFmtTime()} - Something went wrong. Please try again."
    pause(0)
    menu()