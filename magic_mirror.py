# import openpyxl and tkinter modules
# from openpyxl import *
from tkinter import *
from datetime import *
import threading
import time
import requests
import pymsteams

class LiveTime:
    def __init__(self, root):
        # Create a label for the window.
        self.timeLabel = Label(root, text=datetime.now().strftime("%I:%M:%S %p\n%m/%d/%y"), font=("Helvetica", 30), fg="white", bg="black")
        self.timeLabel.pack()

    def update(self):
        self.timeLabel.after(1000, self.update)
        self.timeLabel.config(text=datetime.now().strftime("%I:%M:%S %p\n%m/%d/%Y"))


def main():
    root = Tk()

    # set the background colour of GUI window.
    root.configure(background='black')
    
    # set the title of GUI window
    root.title("Nylex.Net Magic Mirror")
    
    # set the configuration of GUI window.
    root.geometry("500x900")

    root.iconbitmap('favicon.png')

    timer = LiveTime(root)
    timer.update()

    # Testing connectivity to MS Teams.
    myTeamsMessage = pymsteams.connectorcard("<MICROSOFT_WEBHOOK_URL>")
    myTeamsMessage.text("This text was sent using Python.")
    myTeamsMessage.send()

    # start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()