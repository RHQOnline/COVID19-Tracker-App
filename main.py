## Imports
import discord
from discord.ext import commands, tasks
import sys
from os import system, listdir, getcwd
from random import randint, randrange
from termcolor import colored as cld
import COVID19Py

## Pre-Main
def cls():
    system("cls")

def pause(mode=0):
    if mode == 1:
        system("pause")
    elif mode == 2:
        print("pause>nul")
    else:
        print("Nope.")

def setTitle(title):
    system(f"title {title}")

def qExit():
    sys.exit()

## Main(s)
def menu(firstTime=0):
    cls()
    print("Testing.")
    data = covid.getAll()
    pause(1)
    qExit()

def fetchLatest():
    print("poop")

## Script
covid = COVID19Py.COVID19()
menu(1)