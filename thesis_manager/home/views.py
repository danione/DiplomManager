from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



def auth(request):
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('admin_panel')
    else:
        message = 'Save complete'
        return render_to_response('index.html', {message:message})


def home(request):
    return render(request, 'index.html')
