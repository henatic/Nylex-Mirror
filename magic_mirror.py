# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *
from datetime import *
import threading

class TimeThread:
    def startDate():

        date = datetime.now()
        today = date.strftime("%I:%M:%S %m/%d/%y")
        playTime = threading.Thread(target = TimeThread.updateTime(), args=today)
        playTime.start()

    def ampm():
        timeMilitary = time
        pass

    def updateTime():
        newtime = datetime.now().strftime("%I:%M:%S %m/%d/%y")
        if (today != newtime):
            today = newtime


if __name__ == "__main__":
    root = Tk()

    # set the background colour of GUI window.
    root.configure(background='white')
 
    # set the title of GUI window
    root.title("Nylex.net Magic Mirror")
 
    # set the configuration of GUI window.
    root.geometry("500x900")

    # Create a label for the window.
    timeLabel = Label(root, text=TimeThread.startDate())
    timeLabel.pack()

    # heading = Label(root, text=str(datetime.now()))

    # heading.grid(row=0, column=1)


    # start the GUI
    root.mainloop()
