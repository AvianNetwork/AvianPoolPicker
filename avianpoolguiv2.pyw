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
import tkinter as tk
global window
window = tk.Tk()
window.geometry = ("600x600")
window.title = "Avian Pool Picker - Avian Utility by ayonull"
#global area (set globals here)
global allpoolarray
global allpools
global poolkeys
global pools

stratum_array = []
password_array = []
pools = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools.json").json()
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
        try:
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
            password = pools[getpoolfa][2]
            for keys in password:
                password_array.append(keys)
            global passwordkeys
            passwordkeys = password[password_array[1]]
            stratumvar = tk.StringVar()
            stratumvar.set("Pick an Option")
            stratumlist = tk.OptionMenu(window, stratumvar, *poolsarray)
            stratumbutton = tk.Button(window, text="Next", command=lambda: gpc())
            get_strat = stratumvar.get()
            poolbutton.destroy()
            stratumlist.pack()
            stratumbutton.pack()
        except:
            pass
# addr entry
text = tk.StringVar()
ead = tk.Label(text="Enter Avian Address: ")
textbox = tk.Entry(window, textvariable=text)
textbutton = tk.Button(window, text="Next ->", command=lambda: gtm())
#solo or pool
modeget = tk.StringVar()
modemenu = tk.OptionMenu(window, modeget, "Solo", "Pool")
modebutton = tk.Button(window, text="Next ->", command=lambda: gtr())
def gpc():
    strat_get = stratumvar.get()
    if strat_get == "Pick an Option":
        pass
    else:
        ead.pack()
        textbox.pack()
        textbutton.pack()
def gtm():
    global text_get
    text_get = text.get()
    global set_mode
    if password_array[0] == "None":
        password_array.append("x")
    else:
        pass
    modemenu.pack()
    modebutton.pack() 
def gtr():
    global get_modeget
    get_modeget = modeget.get()
    if get_modeget == "Pick an Option":
        pass
    if get_modeget == "Solo":
        password_array.append("m=solo")
    label = (f"minername -o {poolsarray[2]} -u {text_get} -p {password_array[2]}")
    tk.Label(text=label).pack()
    #tk.Label(text="Thank you for using the BETA version of this app. It only goes up till here for now - primitt").pack()
window.mainloop()