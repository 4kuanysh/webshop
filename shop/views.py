from django.shortcuts import render, HttpResponse

def index(requset):
    return HttpResponse("yes")