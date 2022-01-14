import configparser
import enum
from types import TracebackType
from typing import List
import requests
import os
import time
import http
import requests
from colorama import Fore, Back
import signal
import sys
from ping3 import ping
try:
    import clipboard
except ModuleNotFoundError:
    import pyperclip as clipboard
import multiprocessing
import pip
from tkinter import *
ask = input("[1] GPU\n[2] CPU\nPick your hardware(Enter the number): ")
if ask == "1": 
    pools = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools.json").json()
    allpoolarray = []
    allpools = pools
    try:
        for poolkeys in pools:
            allpoolarray.append(poolkeys)
    except KeyError or IndexError:
        print("Could Not find file, please relaunch with internet!")
        exit()
    try:
        for count, poolkey in enumerate(pools, 1):
            print("[",count,"]", poolkey)
    except KeyError:
        print("Error 404: Cannot recive pools.")
# allpoolswf = (f"{allpoolarray}")
# print(f"{allpoolarray}")
    pickpool = input("What pool would you like to pick from the above list? (Pick the number): ")
    try:
        pickpoolint = int(pickpool) -1
        getpoolfa = allpoolarray[pickpoolint]
    except IndexError:
        print("You selected a non integer number.")
    try:
        getpool = pools[getpoolfa][0]
    except KeyError or IndexError:
        print("Unable to parse JSON file! Please try again")
    

    stratums = []
    stratumskeys = []
    choices = []
    try:
    # Enters the keys into the array so that it can be parsed
        for key in getpool:
            stratums.append(key)
            continue
    except KeyError:
        print(Fore.WHITE + "Pool Does not Exist")
        exit()

    try:
        print("Avalible Stratums:")
        for keys in getpool:
            continue
    except:
        print("Pool Does Not exist")
        exit()
    try:
        for choice, keys in enumerate(getpool, 1):
            print("[",choice,"]", keys)
    except KeyError or IndexError:
        print("Index Error")
        print("\nClosing in 6 Seconds...")
        time.sleep(6)
        print("Closing")
        exit()
    askstratum = input("Pick the Stratum (Enter a number): ")
    stratumarray = []
    try:
        for keys in getpool:
            stratumarray.append(keys)
    except KeyError or IndexError:
        print("Index Error")
        print("\nClosing in 6 Seconds...")
        time.sleep(6)
        print("Closing")
        exit()
    try:
        getstratumint = int(askstratum) -1
        getstratumfa = stratumarray[getstratumint]
    except IndexError:
        print("You selected a non integer number.")
    try:
        getstratum = pools[getpoolfa][0][getstratumfa]
    except KeyError or IndexError:
        print("Unable to parse JSON file! Please try again")
    
    askminer = input("Choose the Miner:\n [1] TeamRedMiner \n [2] T-Rex 19.4.1\nPick the corrisponding number: ")
    if askminer == "2":
        choices.append("t-rex.exe")
    if askminer == "1":
        choices.append("teamredminer.exe")
# if askminer == "3":
#     choices.append("cpumineropt.exe")
    choices.append(getstratum)
    askaddress = input("Enter avian Address (Right click to paste): ")
    choices.append(askaddress)
    askmtype = input(
        "[1] Solo or [2] Pool \nPlease choose the number of the mining type you want: ")
    if askmtype == "1":
        choices.append("m=SOLO")
    if askmtype == "2":
        choices.append("x")
# if askminer == "3":
#     askthreads = input("Enter Amount of threads you want to use: ")
#     choices.append(askthreads)
    try:
        cmdlinewf = (f"{choices[0]} -a x16rt -o {choices[1]} -u {choices[2]} -p {choices[3]}")
        clipboard.copy(cmdlinewf)
        print("Command Line: ", choices[0], "-a x16rt -o", choices[1], "-u", choices[2], "-p", choices[3])
        print("\nThis is now copied onto your clipboard!")
        askbatdoc = input("Would you like to create a mining document? (y/n): ")
        if askbatdoc == "y" or askbatdoc == "yes" or askbatdoc == "Yes":
            gpubatdoc = open("mine-gpu.bat", 'x')
            gpubatdoc.write(cmdlinewf)
    except IndexError:
        print("You missed an option!")
if ask == "2":
    cpupools = requests.get("https://aviannetwork.github.io/AvianPoolPicker/poolscpu.json").json()
    cpuallpoolsarray = []
    cpuallpools = cpupools
    try:
        for cpupoolkeys in cpupools:
            cpuallpoolsarray.append(cpupoolkeys)
    except IndexError or KeyError:
        print("Could not find file! Please relaunch")
        time.sleep(5)
        exit()
    try:
        for count, poolkey in enumerate(cpupools, 1):
            print("[",count,"]", poolkey)
    except KeyError or IndexError: 
        print("Could not recive pools! Try again later.")
        time.sleep(5)
        exit()
    cpupickpool = input("What pool would you like to pick from the above list? (Pick the Number): ")
    try:
        cpupickpoolint = int(cpupickpool)-1
        cpugetpoolfa = cpuallpoolsarray[cpupickpoolint]
    except KeyError or IndexError:
        print("You selected a non-integer number")
    try:
        cpugetpool = cpupools[cpugetpoolfa][0]
    except KeyError or IndexError:
        print("Error parsing JSON")
        time.sleep(5)
        exit()
    
    cpustratums = []
    cpustratumkeys = []
    cpuchoices = []
    try:
        for cpukey in cpugetpool:
            cpustratums.append(cpukey)
            continue
    except KeyError or IndexError:
        print("Pool does not exist") 
        time.sleep(5)
        exit()
    try:
        print("Avalible Stratums:")
        for cpukeys in cpugetpool:
            continue;
    except:
        print("Pool does not exist")
        time.sleep(5)
        exit()
    try:
        for choice, cpukeys in enumerate(cpugetpool, 1):
            print("[",choice,"]", cpukeys)
    except KeyError or IndexError:
        print("Index Error")
        print("\nClosing in 6 Seconds...")
        time.sleep(6)
        print("Closing")
        exit()
    cpuaskstratum = input("Pick the Stratum (Enter a number): ")
    cpustratumarray = []
    try:
        for keys in cpugetpool:
            cpustratumarray.append(keys)
    except KeyError or IndexError:
        print("Index Error")
        print("\nClosing in 6 Seconds...")
        time.sleep(6)
        print("Closing")
        exit()
    try:
        cpugetstratumint = int(cpuaskstratum)-1
        cpugetstratumfa = cpustratumarray[cpugetstratumint]
    except IndexError:
        print("You selected a non integer number.")
    try:
        cpugetstratum = cpupools[cpugetpoolfa][0][cpugetstratumfa]
    except KeyError or IndexError:
        print("Unable to parse JSON file! Please try again")
    cpuaskminer = input("Choose the Miner: \n[1] Rplant CPU Miner OPT\nEnter the Number of the Miner you want to pick: ")
    if cpuaskminer == "1":
        cpuchoices.append("cpuminer-sse2.exe")
    cpuchoices.append(cpugetstratum)
    cpuaskaddress = input("Enter avian Address (Right click to paste): ")
    cpuchoices.append(cpuaskaddress)
    cpuaskmtype = input("[1] Solo or [2] Pool \nPlease choose the number of the mining type you want: ")
    if cpuaskmtype == "1":
        cpuchoices.append("c=AVN, m=solo")
    if cpuaskmtype == "2":
        cpuchoices.append("c=AVN")
    cputhreads = (f"How many threads would you like to use? There is a max of {multiprocessing.cpu_count()} threads on your computer: ")
    cpuaskthreads = input(cputhreads)
    cpuchoices.append(cpuaskthreads)
    try:
        cmdlinewf = (f"{cpuchoices[0]} -a minotaurx -o {cpuchoices[1]} -u {cpuchoices[2]} -p {cpuchoices[3]} -t {cpuchoices[4]}")
        clipboard.copy(cmdlinewf)
        print("Command Line: ", cpuchoices[0], "-a minotaurx -o", cpuchoices[1], "-u", cpuchoices[2], "-p", cpuchoices[3], "-t", cpuchoices[4])
        print("\nThis is now copied onto your clipboard!")
        cpuaskwrite = input("Would you like to make a miner file? (y/n): ")
        if cpuaskwrite == "y" or cpuaskwrite == "yes" or cpuaskwrite == "Yes":
            batdoc = open("mine-cpu.bat", 'x')
            batdoc.write(cmdlinewf)
    except IndexError:
        print("You missed an option!")
print("Finished Operation, Closing in 5 seconds automatically...")
time.sleep(5)

