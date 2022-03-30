import configparser
import enum
from types import TracebackType
from typing import List
from itsdangerous import exc
import requests
import os
import time
import http
import requests
from colorama import Fore, Back
import signal
import sys
from ping3 import ping
class get_pools:
    def GPUpools(self):
        self.GPUpool = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools.json").json()
        return self.GPUpool
    def CPUpools():
        global CPUpool
        CPUpool = requests.get("https://aviannetwork.github.io/AvianPoolPicker/poolscpu.json").json()
        return CPUpool
    def miner_file(S):
        global miners
        miners = requests.get("https://aviannetwork.github.io/AvianPoolPicker/miners.json").json()
        return miners
class GPU:
    def idworkersGPU(self, pool, id, walletaddress):
        try:
            Gpool = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools_new.json").json()
            global selection
            poolname = Gpool[pool]
            selection = Gpool[pool][1]['Password']
            if selection == "ID=":
                return (f"ID={id}")
            else:
                return (f"{id}.{walletaddress}")
        except:
            return (f"Unable to get pool with name: {pool}")
    def get_miners(self, miner, platform):
        minerlink = requests.get("https://aviannetwork.github.io/AvianPoolPicker/miners.json").json()
        return minerlink[miner][0][platform]
    def get_password(self, pool, rigname):
        try:
            Gpool = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools_new.json").json()
            password = Gpool[pool][1]["Password"]
            coin = Gpool[pool][1]["Coin"]
            if pool == "ZergPool":
                if rigname == False:
                    if coin == "":
                        format_password = (f"{password}")
                    else:
                        format_password = (f"{coin}")
                    return format_password
                else:
                    if coin == "":
                        format_password = (f"{password},{rigname}")
                    else:
                        format_password = (f"{coin},{rigname}")
                    return format_password
            else:
                    if coin == "":
                        format_password = (f"{password}")
                    else:
                        format_password = (f"{coin}")
                    return format_password
        except:
            print(f"Could not get password of {pool}")
            exit()