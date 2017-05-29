from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import json



def auth(request):
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        message = 'Success'
        return HttpResponse(json.dumps({'message': message}))
    else:
        message = 'Wrong username or password'
        return HttpResponse(json.dumps({'message': message}))


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('admin_panel')
    return render(request, 'index.html')
