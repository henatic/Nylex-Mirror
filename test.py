import requests

obj = {"message": "Help me I need a server :("}

myReq = requests.post('phpTest.php', json=obj)

print(myReq.text)