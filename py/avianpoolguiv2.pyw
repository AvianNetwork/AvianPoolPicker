import configparser
import enum
from pickletools import stringnl_noescape
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
import tkinter as tk
try:
    import clipboard
except ModuleNotFoundError:
    import pyperclip as clipboard
global window
window = tk.Tk()
window.geometry = ("600x600")
window.title = "Avian Pool Picker - Avian Utility by ayonull"
window.configure(bg="#bffffa")
#global area (set globals here)
global allpoolarray
global allpools
global poolkeys
global pools
stratum_array = []
password_array = []
pools = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools.json").json()
print(pools)
allpoolarray = []
allpools = pools
try:
    for poolkeys in pools:
        allpoolarray.append(poolkeys)
except KeyError or IndexError:
    pass
#Get the hardware page
e = tk.StringVar()
e.set("Pick an Option")
hardlist = tk.OptionMenu(window, e, "GPU").pack()
hardbutton = tk.Button(text="Next ->", command=lambda: get_selected())
hardbutton.pack()
# Pool picking page

poolvar = tk.StringVar()
poolvar.set("Pick an Option")
poollist = tk.OptionMenu(window, poolvar, *allpoolarray)
poolbutton = tk.Button(window, text="Next ->", command=lambda: gps())
def get_selected():
    global get_e
    get_e = e.get()
    if get_e == "Pick an Option":
        pass
    else:
        hardbutton.destroy()
        poollist.pack()
        poolbutton.pack()
def gps():
    global pool_op
    pool_op = poolvar.get()
    if pool_op == "Pick an Option":
        pass
    else:
            global ma
            ma = allpoolarray.index(pool_op)
            global getpoolfa
            global getpool
            getpoolfa = allpoolarray[ma]
            getpool = pools[getpoolfa][0]
            global poolsarray
            poolsarray = []
            for keys in getpool:
                poolsarray.append(keys)
            global stratumvar
            global password
            global password_str
            password = pools[getpoolfa][2]["Password"]
            password_str = password.split()
            if password == "None":
                pass
            else:
                for keys in password_str:
                    password_array.append(keys)
            global passwordkeys
            stratumvar = tk.StringVar()
            stratumvar.set("Pick an Option")
            stratumlist = tk.OptionMenu(window, stratumvar, *poolsarray)
            global stratumbutton
            stratumbutton = tk.Button(window, text="Next", command=lambda: gpc())
            get_strat = stratumvar.get()
            poolbutton.destroy()
            stratumlist.pack()
            stratumbutton.pack()
# addr entry
text = tk.StringVar()
ead = tk.Label(text="Enter Avian Address: ")
textbox = tk.Entry(window, textvariable=text)
textbutton = tk.Button(window, text="Next ->", command=lambda: gtm())
#solo or pool
modeget = tk.StringVar()
modeget.set("Pick an Option")
modemenu = tk.OptionMenu(window, modeget, "Solo", "Pool")
modebutton = tk.Button(window, text="Next ->", command=lambda: gtr())
# miner name
json_miners = []
json_miner = requests.get("https://aviannetwork.github.io/AvianPoolPicker/miners.json").json()
for keys in json_miner:
    json_miners.append(keys)
jsonvar = tk.StringVar()
jsonvar.set("Pick an Option")
jsonoption = tk.OptionMenu(window, jsonvar, *json_miners)
jsonbtn = tk.Button(window, text="Next ->", command=lambda: gthw())

def gpc():
    strat_get = stratumvar.get()
    global pool_get
    pool_get = getpool[strat_get]
    if strat_get == "Pick an Option":
        pass
    else:
        ead.pack()
        textbox.pack()
        textbutton.pack()
        stratumbutton.destroy()
def gtm():
    global text_get
    text_get = text.get()
    global set_mode
    if password == "None":
        password_array.append("x")
    else:
        textbutton.destroy()
        pass
    modemenu.pack()
    modebutton.pack()
    textbutton.destroy() 
def gtr():
    global get_modeget
    get_modeget = modeget.get()
    print(modeget.get())
    if get_modeget == "Pick an Option":
        print("passing")
        pass
    def des():
        jsonoption.pack()
        jsonbtn.pack()
        modebutton.destroy()
    if get_modeget == "Solo":
        password_array.append("m=solo")
        des()
    if get_modeget == "Pool":
        des()
    else:
        pass
sofvar = tk.StringVar()
sofvar.set("Pick an Option")
global sofbu
def gthw():
    global get_miner_op
    get_miner_op = jsonvar.get()
    if get_miner_op == "Pick an Option":
        pass
    else:
        global json_miner_index
        global get_soft
        global get_software_ops
        json_miner_index = json_miners.index(get_miner_op)        
        get_soft = json_miner[get_miner_op][0]
        get_software_ops = []
        for keys in get_soft:
            get_software_ops.append(keys)
        print(get_software_ops)
        global strvar
        global strlist
        global strbutton
        strvar = tk.StringVar()
        strvar.set("Pick an Option")
        strlist = tk.OptionMenu(window, strvar, *get_software_ops)
        strbutton = tk.Button(window, text="Next", command=lambda: gidk())
        strlist.pack()
        strbutton.pack()
        jsonbtn.destroy()
#software
def gidk():
    get_str = strvar.get()
    if get_str == "Pick an Option":
        pass
    else:
        get_index_soft = get_software_ops.index(get_str)
        soft = get_soft[get_str]
        print(soft)
        print(password_array)
        try:
            sologet = password_array[1]
            if password_array[0] == "x":
                solo_pass = (f"{sologet}")
            else:
                solo_pass = (f"{password_array[0]}, {sologet}")
            print(password_array, solo_pass)
        except:
            solo_pass = (f"{password_array[0]}")
            print("Not Soloed")
        finallabel = (f"{soft} -a x16rt -o {pool_get} -u {text_get} -p {solo_pass}")
        clipboard.copy(finallabel)
        tk.Label(text=finallabel, font=("Roboto", 11, )).pack()
        tk.Label(text="Copied command line to Clipboard", font=("Roboto", 8)).pack()
tk.Label(window, text="").pack(padx="230")
    # label = (f"minername -o {poolsarray[2]} -u {text_get} -p {password_array[2]}")
    # tk.Label(text=label).pack()
    #tk.Label(text="Thank you for using the BETA version of this app. It only goes up till here for now - primitt").pack()
window.mainloop()