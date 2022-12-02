# import openpyxl and tkinter modules
# # from openpyxl import *
from tkinter import *
from datetime import *
from flask import *
from flask_restful import *
import threading
# import time
# import requests
# import pymsteams
import json
# import jsonify

app = Flask(__name__)

class LiveTime:
    def __init__(self, root):
        # Create a label for the window.
        self.timeLabel = Label(root, text=datetime.now().strftime("%I:%M:%S %p\n%m/%d/%y"), font=("Helvetica", 30), fg="white", bg="black")
        self.timeLabel.pack()

    def update(self):
        self.timeLabel.after(1000, self.update)
        self.timeLabel.config(text=datetime.now().strftime("%I:%M:%S %p\n%m/%d/%Y"))

class TeamData():
    
    def __init__(self):
        # self.emplLabel = Label(root, text='Placeholder for Teams messages.', font=("Helvetica", 15), fg="white", bg="black")
        emplLabel.pack()
        threader = threading.Thread(target=app.run, daemon=True)
        threader.start()

    # def starter():
    #     app.run(debug=)

    @app.route('/', methods=['POST'])
    def response():
        data = json.dumps(request.json)
        data = json.loads(data)
        print(data["message"]["content"])
        emplLabel.config(text=str(data["user"]["displayName"] + " " + data["Date"] + "\n" + data["message"]["content"]))
        return json.dumps({"Success": TRUE})
    
def main():
   
   

    # set the background colour of GUI window.
    root.configure(background='black')
    
    # set the title of GUI window
    root.title("Nylex.Net Magic Mirror")
    
    # set the configuration of GUI window.
    root.geometry("500x900")

    root.iconbitmap('C:\\Users\\henry\\Documents\\Nylex-Mirror\\favicon.ico')

    timer = LiveTime(root)
    timer.update()

    TeamData()
    # Testing connectivity to MS Teams.
    # myTeamsMessage = pymsteams.connectorcard("<WEBHOOK_URL>")
    # myTeamsMessage.text("Bob teh Python Script here.")
    # myTeamsMessage.send()

    # start the GUI
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    emplLabel = Label(root, text='Placeholder for Teams messages.', font=("Helvetica", 15), fg="white", bg="black")
    main()