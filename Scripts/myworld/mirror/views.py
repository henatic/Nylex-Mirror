from django.shortcuts import render
from django.http import HttpResponse
import requests

def recieved(request):
    myReq = requests.post('http://127.0.0.1:5000', json=request)

    return HttpResponse('Posted.')