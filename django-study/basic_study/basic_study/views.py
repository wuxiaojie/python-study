# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect

def hello(request):
#    return HttpResponse("Hello world ! ")
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def haha(request):
    res = HttpResponse()
    res.write("haha")
    return res

from django.http import HttpResponseRedirect
def redfun1(request):
    return HttpResponseRedirect('/haha')


def main(request):
    context = {}
    context["username"] = request.session.get('name', default='guest')
    print context["username"]
    return render(request,"main.html",context)


def login(request):
    return render(request,"login.html")


def showmain(request):
    username = request.POST.get('username')
    print "this is for test"
    # print "%s" %username
    request.session['name'] = username
    return redirect("/main/")

from django.contrib.auth import logout
def quit(request):
    logout(request)
#    request.session.clear()
    return redirect("/login/")

def request_arg(request):
    context = {}
    context["namelist"] = ["ARG1","ARG2","ARG3","ARG4"]
    context["num"] = int(request.GET.get("n"))
    return render(request,"marks.html",context)

def marks(request):
    context = {}
    context["namelist"] = ["Kobe","Harden","James","Ariza"]
    context["num"] = 10
    context["code"] = "<p> this is html escape test! </p>"
    return render(request,"marks.html",context)

def child(request):
    return render(request,"child.html")

def verifycodefile(request):
    f = request.session.get("flag",True)
    context = {}
    context["flag"] = ''
    if not f:
       context["flag"] = "Please input again"
    request.session.clear()
    return render(request,"verifycode.html",context)

def verifycodecheck(request):
    code1 = request.POST.get("verifycode").upper()
    code2 = request.session["verifycode"].upper()
    if code1 == code2:
       return render(request,"success.html")
    else:
       request.session["flag"] = False
       return redirect("/verifycodefile/")
