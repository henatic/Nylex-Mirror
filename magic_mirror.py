# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *
from datetime import *
import threading
import time

# class TimeThread:
#     def __init__(self):
#         return datetime.now().strftime("%I:%M:%S %p\n%m/%d/%y")
#         # print("I want to run, baby!")
#         # playTime = threading.Thread(target = TimeThread.updateTime, args=today)
#         # playTime.start()


#     def ampm():
#         timeMilitary = time
#         pass

#     def updateTime():
#         while(True):
#             newtime = datetime.now().strftime("%I:%M:%S %p\n%m/%d/%y")
#             today = newtime
#             print(today)
#             time.sleep(1)

#     def getTime(self):
#         return self.today

def getTime():
    return datetime.now().strftime("%I:%M:%S %p\n%m/%d/%y")

def update():
    timeLabel.config(text=getTime())
    timeLabel.after(1000, update)

root = Tk()

# set the background colour of GUI window.
root.configure(background='black')
 
# set the title of GUI window
root.title("Nylex.Net Magic Mirror")
 
# set the configuration of GUI window.
root.geometry("500x900")

root.iconbitmap('favicon.png')

# Create a label for the window.
timeLabel = Label(root, text=datetime.now().strftime("%I:%M:%S %p\n%m/%d/%y"), font=("Helvetica", 30), fg="white", bg="black")
timeLabel.pack()
update()
# heading = Label(root, text=str(datetime.now()))

# heading.grid(row=0, column=1)


# start the GUI
root.mainloop()

# if __name__ == "__main__":
#     main()