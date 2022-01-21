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
    def idworkersGPU(self, pool):
            global selection
            GPUpool = requests.get("https://aviannetwork.github.io/AvianPoolPicker/pools.json").json()
            selection = GPUpool[pool]
            if selection == "ZergPool":
                formatzerg = selection[1]["Password"]
                return formatzerg