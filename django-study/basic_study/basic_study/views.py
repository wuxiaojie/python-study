# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

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

import os
from django.conf import settings
#仅支持上传文件
def upload(request):
    if request.method == 'GET':
       return render(request,"upload.html")

    elif request.method == "POST":
       flist = request.FILES.getlist("file",None)
       for f in flist:
         filePath = os.path.join(settings.MEDIA_ROOT,f.name)
         with open(filePath,'wb') as fp:
             for info in f.chunks():
                fp.write(info)
       return HttpResponse("Upload Successfully") 
    else:
       return HttpResponse("Unacceptable http method!!")

#Upload directory, but cannot maintain its structure:
def upload_dir(request):
    if request.method == 'GET':
        return render(request, 'upload_dir.html')
    elif request.method == 'POST':
        dirlist = request.FILES.getlist("upload",None)

        if not dirlist:
            return HttpResponse("Nothing was upload")
        else:
            for file in dirlist:
                file_path = os.path.join(settings.MEDIA_ROOT,str(file))
                with open(file_path, 'wb') as fp:
                   for chunk in file.chunks():
                       fp.write(chunk)
            return HttpResponse("Upload Successfully")
    else:
            return HttpResponseRedirect("Unacceptable http method!!")

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
    

def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，其中FreeMono.ttf可能需要自己下载
    #font = ImageFont.truetype('FreeMono.ttf', 23) 这个会报错IOError: cannot open resource，似乎需要绝对路径
    font = ImageFont.truetype('/root/python_study/django/HelloWorld/HelloWorld/FreeMono.ttf',23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import io
    #buf = io.StringIO() 这个会报错，TypeError: unicode argument expected, got 'str'
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')     
