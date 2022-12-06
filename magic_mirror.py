# import openpyxl and tkinter modules
# # from openpyxl import *
from tkinter import *
from datetime import *
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
        message.pack()
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
            message.config(text=str(wrapper.fill(data["user"]["displayName"] + " " + myTime.strftime("%I:%M:%S %p %m/%d/%Y") + "\n" + re.sub(clean, '', data["message"]["content"]) + message.cget("text"))))
            # user1.config(text=str(wrapper.fill(text=data["user"]["displayName"] + " " + myTime.strftime("%I:%M:%S %p %m/%d/%Y") + "\n" + re.sub(clean, '', data["message"]["content"]))))
            return json.dumps({"Success": TRUE})
        except Exception as e:
            myTeamsMessage.text("The Mirror reflected something ugly caused by the following error:\n" + str(e))
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

    myTeamsMessage.text("Shattered.")
    myTeamsMessage.send()

if __name__ == "__main__":
    root = Tk()
    timeLabel = Label(root, text=datetime.now().strftime("%I:%M:%S %p %m/%d/%y"), font=("Helvetica", 30), fg="white", bg="black")
    message = Label(root, text='', font=("Helvetica", 15), fg="white", bg="black")
    myTeamsMessage = pymsteams.connectorcard("<WEBHOOK_URL>")
    main()