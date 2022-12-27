# import openpyxl and tkinter modules
# # from openpyxl import *
from tkinter import *
from datetime import *
from pytz import timezone
from flask import *
from flask_restful import *
from PIL import Image, ImageTk
import threading
import textwrap
import re
from collections import deque
import random
import pyautogui
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout
import sys
# from io import StringIO
# from html.parser import StringIO
import re
# import time
# import requests
import pymsteams
import json
# import jsonify

class LiveTime:
    def __init__(self):
        # Create a label for the window.
        self.timeLabel.pack()

    def update(self):
        self.timeLabel.after(1000, self.update)
        self.timeLabel.config(text=datetime.now().strftime("%I:%M:%S %p %m/%d/%Y"))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = pyautogui.size()
        self.showFullScreen()
        self.setWindowTitle("Nylex.Net Magic Mirror")

        self.layout = QFormLayout()
        

        self.time = LiveTime()
        self.time.update()

        # self.setCentralWidget(button)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()