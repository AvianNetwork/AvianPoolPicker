import configparser
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
import clipboard
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

pools = requests.get("https://pastebin.com/raw/NAiT5LYh").json()
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
    
allpools = pools

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
askaddress = input("Enter Avain Address (Right click to paste): ")
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
except IndexError:
    print("You missed an option!")
print("Finished Operation, Closing in 20 seconds automatically...")
time.sleep(20)
