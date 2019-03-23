#### iman hasnaouia meskini ###

from django.shortcuts import render
from django.http import HttpResponse
from .form import Login
from time import strftime
import datetime
import calendar
import locale
import json 

def health_check(request):
    locale.setlocale(locale.LC_ALL,'es_ES')
    now = datetime.datetime.now()
    return HttpResponse(str(now.day) + " de " + calendar.month_name[now.month] + " de " + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

def welcome(request):
    wlc = ""
    
    if (request.LANGUAGE_CODE =='es'):
        wlc = "¡Hola mundo!"
    else:
        wlc = "Hello world!"
    
    return HttpResponse(wlc)

#def login(request):
#    return HttpResponse("login")


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            # redirect to a new URL:
            return HttpResponseRedirect('/welcome/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = Login()

    return render(request, 'forms.html', {'form': form})

def check_login(request):
    x = {"status": "error", "code": 401, "message": "User or password not found"}    
    return HttpResponse(json.dumps(x), content_type="application/json")
