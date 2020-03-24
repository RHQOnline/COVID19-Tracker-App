## Imports
import sys
from os import system, listdir, getcwd
from random import randint, randrange
from termcolor import colored as cld
import requests
from datetime import datetime
from time import time, sleep

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

    start_timer = time()

    basicDataFetch = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    parse = basicDataFetch.json()

    cases = parse['cases']
    deaths = parse['deaths']
    recoveries = parse['recovered']
    mortalityRatio = (deaths/(deaths+recoveries))*100

    end_timer = time()
    timerSub = end_timer - start_timer
    timerDisplay = format("%.2f" % timerSub)
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[INFO]", "green"), cld("Global Statistics fetched in [%s seconds].\n" % timerDisplay))

    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Current Confirmed Cases       :   {:,}".format(cases)))
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Current Confirmed Deaths      :   {:,}".format(deaths)))
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Current Confirmed Recoveries  :   {:,}\n".format(recoveries)))
    infectionRate = format("%.3f" % ((cases/7800000000)*100))
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Rounded Infection Ratio       :   %s%%" % infectionRate))
    mortalityRate = format("%.2f" % mortalityRatio)
    print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[DATA]", "green"), cld("Rounded Fatality  Ratio       :   %s%%" % mortalityRate))
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
        sKoreaStrings = ['south korea', 's. korea', 's korea', 'skorea', 'korea south']
        nKoreaStrings = ['north korea', 'n. korea', 'n korea', 'nkorea', 'korea north']
        diamondPrincessStrings = ['diamond princess', 'dprincess', 'diamondprince']
        arabiaStrings = ['saudi arabia', 'arabia', 'saudi', 'saudiarabia']
        hongKongStrings = ['hong kong', 'hongkong', 'hongk', 'hkong']
        africaStrings = ['south africa', 'safrica', 'southafrica', 's. africa', 's africa']
        sanMarinoStrings = ['san marino', 'sanmarino', 'marino']
        costaRicaStrings = ['costa rica', 'costarica']
        bosniaAndHerzegovinaStrings = ['bosnia and herzegovina', 'bosnia', 'herzegovina']
        faroeIslandsStrings = ['faroe', 'islands', 'faroe islands', 'faroeislands']
        northMacedoniaStrings = ['north macedonia', 'n. macedonia', 'n macedonia', 'northmacedonia']
        sriLankaStrings = ['sri lanka', 'sri', 'lanka', 'srilanka']
        dominicanRepublicStrings = ['dominican republic', 'dominican', 'drepublic', 'dominicanrepublic']
        nzStrings = ['new zealand', 'zealand', 'newzealand', 'n zealand']
        burkinaFasoStrings = ['burkina faso', 'burkinafaso', 'burkina']
        frenchGuianaStrings = ['french guiana', 'frenchguiana', 'guiana', 'fguiana']
        puertoRicoStrings = ['puerto rice', 'puertorico']
        channelIslandsStrings = ['channel islands', 'channelislands', 'channislands']
        frenchPolynesiaStrings = ['french polynesia', 'frenchpolynesia', 'fpolynesia', 'polynesia']
        ivoryCoastStrings = ['ivory coast', 'ivorycoast', 'ivycoast']
        trinTobStrings = ['trinidad', 'tobago', 'trinidad and tobago', 'tat']
        eqGuineaStrings = ['equatorial guinea', 'equatorialguinea', 'eqguinea']
        stMartinStrings = ['saint martin', 'stmartin', 'st martin', 'saintmartin']
        cayIslStrings = ['cayman islands', 'caymanislands', 'cayman']
        stBarthStrings = ['saint barth', 'saintbarth', 'stbarth', 'st barth']
        usVgIslStrings = ['u.s. virgin islands', 'u.s. virgin island', 'virgin islands', 'virginislands', 'usvirginislands', 'us virgin islands', 'us virgin islands', 'united states virgin islands']
        isleOfManStrings = ['isle of man', 'isleofman']
        newCalStrings = ['new caledonia', 'newcaledonia', 'newcal', 'caledonia']
        stLuciaStrings = ['stlucia', 'st lucia', 'saint lucia', 'saintlucia']
        antigBarbuStrings = ['antigua', 'barbuda', 'antigua and barbuda']
        caboVerdeStrings = ['cabo verde', 'caboverde']
        elSalvStrings = ['el salvador', 'elsalvador', 'salvador', 'elsal']
        vaticanStrings = ['vatican city', 'the vatican city', 'vaticancity', 'vatican']
        stVincGrenStrings = ['saint vincent', 'st vincent', 'saintvincent', 'stvincent', 'saint vincent and the grenadines', 'saintvincentandthegrenadines', 'stvincentandthegrenadines', 'st vincent and the grenadines']
        sintMaartenStrings = ['sint maarten', 'sintmaarten', 'maarten']
        countryName = country
        if country.lower() in uaeStrings:
            countryName = "uae"
        elif country.lower() in ukStrings:
            countryName = "uk"
        elif country.lower() in usStrings:
            countryName = "usa"
        elif country.lower() in sKoreaStrings:
            countryName = "s. korea"
        if country.lower() in nKoreaStrings:
            countryName = "s. korea"
        if country.lower() in diamondPrincessStrings:
            countryName = "diamond princess"
        if country.lower() in arabiaStrings:
            countryName = "saudi arabia"
        if country.lower() in hongKongStrings:
            countryName = "hong kong"
        if country.lower() in africaStrings:
            countryName = "south africa"
        if country.lower() in sanMarinoStrings:
            countryName = "san marino"
        if country.lower() in costaRicaStrings:
            countryName = "costa rica"
        if country.lower() in bosniaAndHerzegovinaStrings:
            countryName = "bosnia and herzegovina"
        if country.lower() in faroeIslandsStrings:
            countryName = "faroe islands"
        if country.lower() in northMacedoniaStrings:
            countryName = "north macedonia"
        if country.lower() in sriLankaStrings:
            countryName = "sri lanka"
        if country.lower() in dominicanRepublicStrings:
            countryName = "dominican republic"
        if country.lower() in nzStrings:
            countryName = "new zealand"
        if country.lower() in burkinaFasoStrings:
            countryName = "burkina faso"
        if country.lower() in frenchGuianaStrings:
            countryName = "french guiana"
        if country.lower() in puertoRicoStrings:
            countryName = "puerto rico"
        if country.lower() in channelIslandsStrings:
            countryName = "channel islands"
        if country.lower() in frenchPolynesiaStrings:
            countryName = "french polynesia"
        if country.lower() in ivoryCoastStrings:
            countryName = "ivory coast"
        if country.lower() in trinTobStrings:
            countryName = "trinidad and tobago"
        if country.lower() in eqGuineaStrings:
            countryName = "equatorial guinea"
        if country.lower() in stMartinStrings:
            countryName = "saint martin"
        if country.lower() in cayIslStrings:
            countryName = "cayman islands"
        if country.lower() in stBarthStrings:
            countryName = "st. barth"
        if country.lower() in usVgIslStrings:
            countryName = "u.s. virgin islands"
        if country.lower() in isleOfManStrings:
            countryName = "isle of man"
        if country.lower() in newCalStrings:
            countryName = "new caledonia"
        if country.lower() in stLuciaStrings:
            countryName = "saint lucia"
        if country.lower() in antigBarbuStrings:
            countryName = "antigua and barbuda"
        if country.lower() in caboVerdeStrings:
            countryName = "cabo verde"
        if country.lower() in elSalvStrings:
            countryName = "el salvador"
        if country.lower() in vaticanStrings:
            countryName = "vatican city"
        if country.lower() in stVincGrenStrings:
            countryName = "st. vincent grenadines"
        if country.lower() in sintMaartenStrings:
            countryName = "sint maarten"
        start_timer = time()
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
        stop_timer = time()
        timerDisplayFmt = format("%.2f" % (stop_timer - start_timer))
        displaySearchResults(country, cases, deaths, recovered, active, critical, casesPOM, tdCases, tdDeaths, timerDisplayFmt)
    elif isAltName == False:
        start_timer = time()
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
        stop_timer = time()
        timerDisplayFmt = format("%.2f" % (stop_timer - start_timer))
        displaySearchResults(country, cases, deaths, recovered, active, critical, casesPOM, tdCases, tdDeaths, timerDisplayFmt)

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f %s' % (num, ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Pentillion'][magnitude])

def displaySearchResults(country, cases, deaths, recovered, active, critical, casesPOM, tdCases, tdDeaths, timeDisplayFmt):
    try:
        cls()
        print(cld("[RHQOnline]", "green"), cld("The results displayed below are detailed, legitimate statistics."))
        print(cld("[RHQOnline]", "green"), cld("The results are updated hourly via the CDC and WHO."))
        print(cld("[RHQOnline]", "green"), cld("This dataset query took [%s seconds] to complete." % timeDisplayFmt))
        print(cld("[RHQOnline]", "green"), cld("You are fetching this dataset at %s on %s.\n\n" % (getFmtTime(), getFmtDate())))

        try:
            mortalityRatio = (deaths/(deaths+recovered))*100
        except ZeroDivisionError as zde:
            print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[ERROR]", "red"), cld("%s - Mortality Rate cannot be obtained. [0 recoveries in region.]\n" % zde))
            mortalityRatio = 0

        countryPop = (cases/casesPOM)*1000000
        # countryPopDisplay = format("%:,.2f" % countryPop)
        infectionRate = (cases/(countryPop))*100
        infectionRateDisplay = format("%.4f" % infectionRate)

        # deaths_to_recovered = (deaths/recovered)*100

        countryPopDisplay = human_format(countryPop)

        print(cld("[DATA]", "green"), cld("Country in Question          :   %s" % country))
        print(cld("[DATA]", "green"), cld("Total Population of Country  :   %s" % countryPopDisplay))
        print(cld("[DATA]", "green"), cld("---------------------------------------------------"))
        print(cld("[DATA]", "green"), cld("Total Confirmed Cases        :   {:,}".format(cases)))
        print(cld("[DATA]", "green"), cld("Total Cases Today            :   {:,}".format(tdCases)))
        print(cld("[DATA]", "green"), cld("Total Confirmed Deaths       :   {:,}".format(deaths)))
        print(cld("[DATA]", "green"), cld("Total Deaths Today           :   {:,}".format(tdDeaths)))
        print(cld("[DATA]", "green"), cld("Total Confirmed Recoveries   :   {:,}".format(recovered)))
        print(cld("[DATA]", "green"), cld("---------------------------------------------------"))
        print(cld("[DATA]", "green"), cld("Total Active Cases           :   {:,}".format(active)))
        print(cld("[DATA]", "green"), cld("Total in Critical Condition  :   {:,}".format(critical)))
        print(cld("[DATA]", "green"), cld("Cases per One Million        :   {:,}".format(casesPOM)))
        print(cld("[DATA]", "green"), cld("---------------------------------------------------"))
        mortalityRate = format("%.4f" % mortalityRatio)
        print(cld("[DATA]", "green"), cld("Rounded Infection Ratio      :   %s%%" % infectionRateDisplay)) # , cld("[DISABLED]", "red")
        print(cld("[DATA]", "green"), cld("Rounded Fatality  Ratio      :   %s%%" % mortalityRate))

        print(cld("\n\n[RHQOnline]", "green"), cld("Press any key to try again, or 'CTRL+C' to exit..."))
        pause(1)
        mainFxn()
    except:
        print(cld("\n" + getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[ERROR]", "red"), cld("An error occured whilst fetching / displaying the data.")) # f"{getFmtDate()} {getFmtTime()} - Something went wrong. Please try again."
        print(cld(getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[ERROR]", "red"), cld("Press any key to try again..."))
        pause(1)
        mainFxn()

def checkForExceptions(country):
    uaeStrings = ['united arab emirates', 'arab emirates', 'united arab', 'emirates', 'unitedarabemirates', 'the uae']
    ukStrings = ['scotland', 'united kingdom', 'unitedkingdom', 'the uk']
    usStrings = ['america', 'united states', 'united states of america', 'the us', 'the usa']
    sKoreaStrings = ['south korea', 's. korea', 's korea', 'skorea', 'korea south']
    nKoreaStrings = ['north korea', 'n. korea', 'n korea', 'nkorea', 'korea north']
    diamondPrincessStrings = ['diamond princess', 'dprincess', 'diamondprince']
    arabiaStrings = ['saudi arabia', 'arabia', 'saudi', 'saudiarabia']
    hongKongStrings = ['hong kong', 'hongkong', 'hongk', 'hkong']
    africaStrings = ['south africa', 'safrica', 'southafrica', 's. africa', 's africa']
    sanMarinoStrings = ['san marino', 'sanmarino', 'marino']
    costaRicaStrings = ['costa rica', 'costarica']
    bosniaAndHerzegovinaStrings = ['bosnia and herzegovina', 'bosnia', 'herzegovina']
    faroeIslandsStrings = ['faroe', 'islands', 'faroe islands', 'faroeislands']
    northMacedoniaStrings = ['north macedonia', 'n. macedonia', 'n macedonia', 'northmacedonia']
    sriLankaStrings = ['sri lanka', 'sri', 'lanka', 'srilanka']
    dominicanRepublicStrings = ['dominican republic', 'dominican', 'drepublic', 'dominicanrepublic']
    nzStrings = ['new zealand', 'zealand', 'newzealand', 'n zealand']
    burkinaFasoStrings = ['burkina faso', 'burkinafaso', 'burkina']
    frenchGuianaStrings = ['french guiana', 'frenchguiana', 'guiana', 'fguiana']
    puertoRicoStrings = ['puerto rice', 'puertorico']
    channelIslandsStrings = ['channel islands', 'channelislands', 'channislands']
    frenchPolynesiaStrings = ['french polynesia', 'frenchpolynesia', 'fpolynesia', 'polynesia']
    ivoryCoastStrings = ['ivory coast', 'ivorycoast', 'ivycoast']
    trinTobStrings = ['trinidad', 'tobago', 'trinidad and tobago', 'tat']
    eqGuineaStrings = ['equatorial guinea', 'equatorialguinea', 'eqguinea']
    stMartinStrings = ['saint martin', 'stmartin', 'st martin', 'saintmartin']
    cayIslStrings = ['cayman islands', 'caymanislands', 'cayman']
    stBarthStrings = ['saint barth', 'saintbarth', 'stbarth', 'st barth']
    usVgIslStrings = ['u.s. virgin islands', 'u.s. virgin island', 'virgin islands', 'virginislands', 'usvirginislands', 'us virgin islands', 'us virgin islands', 'united states virgin islands']
    isleOfManStrings = ['isle of man', 'isleofman']
    newCalStrings = ['new caledonia', 'newcaledonia', 'newcal', 'caledonia']
    stLuciaStrings = ['stlucia', 'st lucia', 'saint lucia', 'saintlucia']
    antigBarbuStrings = ['antigua', 'barbuda', 'antigua and barbuda']
    caboVerdeStrings = ['cabo verde', 'caboverde']
    elSalvStrings = ['el salvador', 'elsalvador', 'salvador', 'elsal']
    vaticanStrings = ['vatican city', 'the vatican city', 'vaticancity', 'vatican']
    stVincGrenStrings = ['saint vincent', 'st vincent', 'saintvincent', 'stvincent', 'saint vincent and the grenadines', 'saintvincentandthegrenadines', 'stvincentandthegrenadines', 'st vincent and the grenadines']
    sintMaartenStrings = ['sint maarten', 'sintmaarten', 'maarten']
    # Strings = []

    if country.lower() in uaeStrings:
        return True
    if country.lower() in ukStrings:
        return True
    if country.lower() in usStrings:
        return True
    if country.lower() in sKoreaStrings:
        return True
    if country.lower() in nKoreaStrings:
        return True
    if country.lower() in diamondPrincessStrings:
        return True
    if country.lower() in arabiaStrings:
        return True
    if country.lower() in hongKongStrings:
        return True
    if country.lower() in africaStrings:
        return True
    if country.lower() in sanMarinoStrings:
        return True
    if country.lower() in costaRicaStrings:
        return True
    if country.lower() in bosniaAndHerzegovinaStrings:
        return True
    if country.lower() in faroeIslandsStrings:
        return True
    if country.lower() in northMacedoniaStrings:
        return True
    if country.lower() in sriLankaStrings:
        return True
    if country.lower() in dominicanRepublicStrings:
        return True
    if country.lower() in nzStrings:
        return True
    if country.lower() in burkinaFasoStrings:
        return True
    if country.lower() in frenchGuianaStrings:
        return True
    if country.lower() in puertoRicoStrings:
        return True
    if country.lower() in channelIslandsStrings:
        return True
    if country.lower() in frenchPolynesiaStrings:
        return True
    if country.lower() in ivoryCoastStrings:
        return True
    if country.lower() in trinTobStrings:
        return True
    if country.lower() in eqGuineaStrings:
        return True
    if country.lower() in stMartinStrings:
        return True
    if country.lower() in cayIslStrings:
        return True
    if country.lower() in stBarthStrings:
        return True
    if country.lower() in usVgIslStrings:
        return True
    if country.lower() in isleOfManStrings:
        return True
    if country.lower() in newCalStrings:
        return True
    if country.lower() in stLuciaStrings:
        return True
    if country.lower() in antigBarbuStrings:
        return True
    if country.lower() in caboVerdeStrings:
        return True
    if country.lower() in elSalvStrings:
        return True
    if country.lower() in vaticanStrings:
        return True
    if country.lower() in stVincGrenStrings:
        return True
    if country.lower() in sintMaartenStrings:
        return True
    else:
        return False

def mainFxn():
    try:
        menu()
    except KeyboardInterrupt:
        print(cld("\n\n" + getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[INFO]", "yellow"), cld("Manual Hault Detected. Exiting..."))
        pause(0)
        qExit()
    except:
        print(cld("\n" + getFmtDate(), "green"), cld(getFmtTime(), "green"), cld("[ERROR]", "red"), cld("Invalid country entered. Please try again.")) # f"{getFmtDate()} {getFmtTime()} - Something went wrong. Please try again."
        pause(0)
        mainFxn()

## Script
setTitle("RHQOnline's nCov COVID19 Tracker")
mainFxn()