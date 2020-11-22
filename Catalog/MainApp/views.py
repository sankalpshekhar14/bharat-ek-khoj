from django.shortcuts import render
import pymongo
from .recieve import Recieve

def index(request):
    recieving_thread=Recieve()
    recieving_thread.start()
    recieving_thread.make_connection()
    return HttpResponse("<h1>Request recieved</h1>")
