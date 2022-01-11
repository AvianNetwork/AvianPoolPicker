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
    import Tkinter as tk
except:
    import tkinter as tk

window = tk.Tk()
window.title("Avian Pool Picker")
window.iconbitmap('./icon.ico')
window.geometry("600x600")
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
        tk.Frame.__init__(self, master)
        clicked = tk.StringVar()
        clicked.set("Pick an Option")
        drop = tk.OptionMenu(window, clicked, "GPU", "CPU").pack()
        tk.Button(self, text="Next ->",
                command=lambda: master.switch_frame(PageOne)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=5)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
