# import openpyxl and tkinter modules
# # from openpyxl import *
from tkinter import *
from datetime import *
from pytz import timezone
from flask import *
from flask_restful import *
import threading
import textwrap
import re
from collections import deque
# from io import StringIO
# from html.parser import StringIO
import re
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
        user1.pack()
        message1.pack()
        user2.pack()
        message2.pack()
        user3.pack()
        message3.pack()
        user4.pack()
        message4.pack()
        user5.pack()
        message5.pack()
        user6.pack()
        message6.pack()
        user7.pack()
        message7.pack()
        user8.pack()
        message8.pack()
        # self.template()

    # def template(self, name="Bob", mess='Foo'):
    #     with app.app_context():
    #         return render_template('index.html', title='Hey Sexy.', displayName=name, content=mess)

    @app.route('/', methods=['POST'])
    def response():
        try:
            data = json.dumps(request.json)
            data = json.loads(data)
            wrapper = textwrap.TextWrapper(width=50)
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
                userList.appendleft(toTop)
                msgList.remove(msgList[getIndex])
                msgList.appendleft(re.sub(clean, '', data["message"]["content"]))
                timeStamp.remove(timeStamp[getIndex])
                timeStamp.appendleft(myTime.strftime("%I:%M:%S %p %m/%d/%Y"))
            else:
                userList.appendleft(data["user"]["displayName"])
                timeStamp.appendleft(myTime.strftime("%I:%M:%S %p %m/%d/%Y"))
                msgList.appendleft(re.sub(clean, '', data["message"]["content"]))
            if len(userList) > 9:
                userList.pop()
                msgList.pop()
                timeStamp.pop()
            
            user1.config(text=userList[0] + " " + timeStamp[0])
            message1.config(text=str(wrapper.fill(msgList[0])))
            if len(msgList) >= 2:
                user2.config(text=userList[1] + " " + timeStamp[1])
                message2.config(text=str(wrapper.fill(msgList[1])))
            if len(msgList) >= 3:
                user3.config(text=userList[2] + " " + timeStamp[2])
                message3.config(text=str(wrapper.fill(msgList[2])))
            if len(msgList) >= 4:
                user4.config(text=userList[3] + " " + timeStamp[3])
                message4.config(text=str(wrapper.fill(msgList[3])))
            if len(msgList) >= 5:
                user5.config(text=userList[4] + " " + timeStamp[4])
                message5.config(text=str(wrapper.fill(msgList[4])))
            if len(msgList) >= 6:
                user6.config(text=userList[5] + " " + timeStamp[5])
                message6.config(text=str(wrapper.fill(msgList[5])))
            if len(msgList) >= 7:
                user7.config(text=userList[6] + " " + timeStamp[6])
                message7.config(text=str(wrapper.fill(msgList[6])))
            if len(msgList) >= 8:
                user8.config(text=userList[7] + " " + timeStamp[7])
                message8.config(text=str(wrapper.fill(msgList[7])))
            # user1.config(text=str(wrapper.fill(text=data["user"]["displayName"] + " " + myTime.strftime("%I:%M:%S %p %m/%d/%Y") + "\n" + re.sub(clean, '', data["message"]["content"]))))
            return json.dumps({"Success": TRUE})
        except Exception as e:
            myTeamsMessage.text("I reflected something ugly-looking:\n" + str(e) + ".\nData Recieved: " + str(data))
            myTeamsMessage.send()
    
def main():

    # set the background colour of GUI window.
    root.configure(background='black')
    
    # set the title of GUI window
    root.title("Nylex.Net Magic Mirror")
    
    # set the configuration of GUI window.
    root.geometry("500x900")

    root.iconbitmap('C:\\Users\\henry\\Documents\\Nylex-Mirror\\favicon.ico')

    timer = LiveTime()
    timer.update()
    
    TeamData()

    # Testing connectivity to MS Teams.
    myTeamsMessage.text("I am now reflecting.")
    myTeamsMessage.send()

    # start the GUI
    root.mainloop()

    myTeamsMessage.text("Shattered into pieces.")
    myTeamsMessage.send()

if __name__ == "__main__":
    root = Tk()
    timeLabel = Label(root, text=datetime.now().strftime("%I:%M:%S %p %m/%d/%y"), font=("Helvetica", 30), fg="white", bg="black")

    user1 = Label(root, text='', font=("Helvetica", 15), fg="green", bg="black")
    user2 = Label(root, text='', font=("Helvetica", 15), fg="blue", bg="black")
    user3 = Label(root, text='', font=("Helvetica", 15), fg="grey", bg="black")
    user4 = Label(root, text='', font=("Helvetica", 15), fg="green", bg="black")
    user5 = Label(root, text='', font=("Helvetica", 15), fg="blue", bg="black")
    user6 = Label(root, text='', font=("Helvetica", 15), fg="grey", bg="black")
    user7 = Label(root, text='', font=("Helvetica", 15), fg="green", bg="black")
    user8 = Label(root, text='', font=("Helvetica", 15), fg="blue", bg="black")

    message1 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message2 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message3 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message4 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message5 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message6 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message7 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    message8 = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")

    userList = deque()
    msgList = deque()
    timeStamp = deque()
    myTeamsMessage = pymsteams.connectorcard("WEBHOOK_URL")
    main()