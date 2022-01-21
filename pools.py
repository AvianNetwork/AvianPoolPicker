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
class GPU:
    def idworkersGPU(self, pool, id):
        try:
            Gpool = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools_new.json").json()
            global selection
            poolname = Gpool[pool]
            selection = Gpool[pool][1]['Password']
            if selection == "ID=":
                return (f"ID={id}")
        except:
            return (f"Unable to get pool with name: {pool}")