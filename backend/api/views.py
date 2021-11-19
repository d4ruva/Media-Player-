from django.http.response import HttpResponse
from django.shortcuts import render

'''FireBase Connection'''
from firebase import firebase

firebase = firebase.FirebaseApplication("https://media-player-8422a-default-rtdb.firebaseio.com/", None)

data = {
    'Name': "test",
}

result = firebase.post('media-player-8422a-default-rtdb', data)
print(result)

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

