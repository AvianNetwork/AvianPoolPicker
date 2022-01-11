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


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
            def get_selected():
                get_e = e.get()
                print(get_e)
                if get_e == "Pick an Option":
                    pass
                else:
                    master.switch_frame(PageOne)
            tk.Frame.__init__(self, master)
            e = tk.StringVar()
            e.set("Pick an Option")
            hello = tk.OptionMenu(master,e, "GPU", "CPU").pack()
            otherbutton = tk.Button(text="Next ->", command=lambda: get_selected()).pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="Avian Network is Kool", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                command=lambda: master.switch_frame(StartPage)).pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
