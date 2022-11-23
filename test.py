import requests

obj = {"message": "Help me I need a server :("}

myReq = requests.post('http://10.10.99.152:5000', json=obj)

print(myReq.text)