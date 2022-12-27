# import openpyxl and tkinter modules
# # from openpyxl import *
# from reader.__main__ import main
from tkinter import *
from datetime import *
from pytz import timezone
from flask import *
from flask_restful import *
from PIL import Image, ImageTk
from waitress import serve
import threading
import uvicorn
import textwrap
import re
from collections import deque
import random
import pyautogui
import PyQt6
# from io import StringIO
# from html.parser import StringIO
# import time
# import requests
import pymsteams
import json
# import jsonify

app = Flask(__name__)

class LiveTime:
    def __init__(self):
        # Create a label for the window.
        timeLabel.pack()

    def update(self):
        timeLabel.after(1000, self.update)
        timeLabel.config(text=datetime.now().strftime("%I:%M:%S %p %m/%d/%Y"))

class TeamData():
    
    def __init__(self):
        # self.user1 = Label(root, text='Placeholder for Teams messages.', font=("Helvetica", 15), fg="white", bg="black")

        threader = threading.Thread(target=app.run, daemon=True)
        threader.start()
        # user1.pack(anchor=W)
        # message1.pack(pady=(0, 10), anchor=W)
        # user2.pack(anchor=W)
        # message2.pack(pady=(0, 10), anchor=W)
        # user3.pack(anchor=W)
        # message3.pack(pady=(0, 10), anchor=W)
        # user4.pack(anchor=W)
        # message4.pack(pady=(0, 10), anchor=W)
        # user5.pack(anchor=W)
        # message5.pack(pady=(0, 10), anchor=W)
        # user6.pack(anchor=W)
        # message6.pack(pady=(0, 10), anchor=W)
        # user7.pack(anchor=W)
        # message7.pack(pady=(0, 10), anchor=W)
        # user8.pack(anchor=W)
        # message8.pack(pady=(0, 10), anchor=W)
        # line.pack(anchor=W)
        # orderStatus.pack()
        # self.template()

    # def template(self, name="Bob", mess='Foo'):
    #     with app.app_context():
    #         return render_template('index.html', title='Hey Sexy.', displayName=name, content=mess)

    @app.route('/', methods=['POST'])
    def response():
        try:
            data = json.dumps(request.json)
            data = json.loads(data)
            wrapper = textwrap.TextWrapper(width=int(window.width / 2))
            clean = re.compile('<.*?>')
            myTime = datetime.strptime(data["Date"], '%Y-%m-%dT%H:%M:%S.%fZ')
            myTime = myTime.replace(tzinfo=timezone('UTC'))
            myTime = myTime.astimezone(timezone('US/Pacific'))
            getIndex = 0
            if data["user"]["displayName"] in userList:
                toTop = data["user"]["displayName"]
                while(userList[getIndex] != data["user"]["displayName"]):
                    getIndex += 1
                userList.remove(data["user"]["displayName"])
                userColor = colorList[getIndex]
                colorList.remove(userColor)
                userList.appendleft(toTop)
                msgList.remove(msgList[getIndex])
                msgList.appendleft(re.sub(clean, '', data["message"]["content"]))
                colorList.appendleft(userColor)
                timeStamp.remove(timeStamp[getIndex])
                timeStamp.appendleft(myTime.strftime("%I:%M:%S %p %m/%d/%Y"))
            else:
                userList.appendleft(data["user"]["displayName"])
                timeStamp.appendleft(myTime.strftime("%I:%M:%S %p %m/%d/%Y"))
                msgList.appendleft(re.sub(clean, '', data["message"]["content"]))
                userColor = colorList.pop()
                colorList.appendleft(userColor)
                labelList.append(Label(root, text=userList[0] + " " + timeStamp[0], font=("Helvetica", 15), fg=colorList[0], bg="black"))
                labelMsg.append(Label(root, text=msgList[0], font=("Helvetica", 15), fg="white", bg="black", width=int(window.width / 2)))
                labelList[-1].pack(anchor=W)
                labelMsg[-1].pack(anchor=E)

            index = 0
            colorIndex = 0
            while index < len(labelList) and index < len(labelMsg):
                if colorIndex >= len(colorList):
                    colorIndex = 0
                labelList[index].config(text=userList[index] + " " + timeStamp[index], fg=colorList[index], justify=LEFT)
                labelMsg[index].config(text=str(wrapper.fill(msgList[index])), justify=LEFT)
                index += 1
                colorIndex += 1
            # if len(userList) > 9:
            #     userList.pop()
            #     msgList.pop()
            #     timeStamp.pop()

            # user1.config(text=userList[0] + " " + timeStamp[0], fg=colorList[0], justify=LEFT)
            # message1.config(text=str(wrapper.fill(msgList[0])), justify=LEFT)
            # if len(msgList) >= 2:
            #     user2.config(text=userList[1] + " " + timeStamp[1], fg=colorList[1], justify=LEFT)
            #     message2.config(text=str(wrapper.fill(msgList[1])), justify=LEFT)
            # if len(msgList) >= 3:
            #     user3.config(text=userList[2] + " " + timeStamp[2], fg=colorList[2], justify=LEFT)
            #     message3.config(text=str(wrapper.fill(msgList[2])), justify=LEFT)
            # if len(msgList) >= 4:
            #     user4.config(text=userList[3] + " " + timeStamp[3], fg=colorList[3], justify=LEFT)
            #     message4.config(text=str(wrapper.fill(msgList[3])), justify=LEFT)
            # if len(msgList) >= 5:
            #     user5.config(text=userList[4] + " " + timeStamp[4], fg=colorList[4], justify=LEFT)
            #     message5.config(text=str(wrapper.fill(msgList[4])), justify=LEFT)
            # if len(msgList) >= 6:
            #     user6.config(text=userList[5] + " " + timeStamp[5], fg=colorList[5], justify=LEFT)
            #     message6.config(text=str(wrapper.fill(msgList[5])), justify=LEFT)
            # if len(msgList) >= 7:
            #     user7.config(text=userList[6] + " " + timeStamp[6], fg=colorList[6], justify=LEFT)
            #     message7.config(text=str(wrapper.fill(msgList[6])), justify=LEFT)
            # if len(msgList) >= 8:
            #     user8.config(text=userList[7] + " " + timeStamp[7], fg=colorList[7], justify=LEFT)
            #     message8.config(text=str(wrapper.fill(msgList[7])), justify=LEFT)
            # user1.config(text=str(wrapper.fill(text=data["user"]["displayName"] + " " + myTime.strftime("%I:%M:%S %p %m/%d/%Y") + "\n" + re.sub(clean, '', data["message"]["content"]))))
            return json.dumps({"Success": TRUE})
        except Exception as e:
            myTeamsMessage.text("I reflected something ugly-looking:\n" + str(e) + ".\nData Recieved: " + str(data))
            myTeamsMessage.send()
    
def main():

    # set the background colour of GUI window.
    root.configure(background='black', cursor='none')
    
    # set the title of GUI window
    root.title("Nylex.Net Magic Mirror")
    
    # set the configuration of GUI window.
    # root.geometry(str(500) + "x" + str(900))
    root.attributes('-fullscreen', True)

    root.iconbitmap('C:\\Users\\henry\\Documents\\Nylex-Mirror\\favicon.ico')

    timer = LiveTime()
    timer.update()
    
    TeamData()

    # Testing connectivity to MS Teams.
    myTeamsMessage.text("I am now reflecting.")
    myTeamsMessage.send()

    # start the GUI
    root.mainloop()

    myTeamsMessage.text("Shattered.")
    myTeamsMessage.send()

if __name__ == "__main__":

    root = Tk()
    timeLabel = Label(root, text=datetime.now().strftime("%I:%M:%S %p %m/%d/%y"), font=("Helvetica", 50), fg="white", bg="black")

    colorList = deque(['red', 'OrangeRed', 'yellow', 'Lime', 'DeepSkyBlue', 'magenta', 'BurlyWood', 'Turquoise'])
    random.shuffle(colorList)

    window = pyautogui.size()

    # user1 = Label(root, text='', font=("Helvetica", 15), fg=colorList[0], bg="black")
    # user2 = Label(root, text='', font=("Helvetica", 15), fg=colorList[1], bg="black")
    # user3 = Label(root, text='', font=("Helvetica", 15), fg=colorList[2], bg="black")
    # user4 = Label(root, text='', font=("Helvetica", 15), fg=colorList[3], bg="black")
    # user5 = Label(root, text='', font=("Helvetica", 15), fg=colorList[4], bg="black")
    # user6 = Label(root, text='', font=("Helvetica", 15), fg=colorList[5], bg="black")
    # user7 = Label(root, text='', font=("Helvetica", 15), fg=colorList[6], bg="black")
    # user8 = Label(root, text='', font=("Helvetica", 15), fg=colorList[7], bg="black")

    # message1 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message2 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message3 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message4 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message5 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message6 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message7 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    # message8 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")

    # line = Canvas(master=root, width=window.width, height=1, bg="white")

    # orderStatus = Label(root, text='<Shipping status goes here.>', font=("Helvetica", 15), fg="white", bg="black")

    userList = deque()
    msgList = deque()
    timeStamp = deque()
    labelList = deque()
    labelMsg = deque()

    myTeamsMessage = pymsteams.connectorcard("https://nylexnet.webhook.office.com/webhookb2/44d40371-f594-4635-b0f4-54d864f70239@acb14216-43ac-4962-b25b-189ff1152188/IncomingWebhook/1c0324112a1c4e9f88ca0d8d748bc20d/452c7170-efff-49e4-ad6d-f3026a67c734")
    main()
