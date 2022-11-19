import requests

obj = 'Posty toasty'

myReq = requests.post('http://127.0.0.1:5000', json=obj)

print(myReq.text)