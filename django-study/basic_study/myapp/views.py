# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Grade,Student
def grades(request):
    gradesList = Grade.objects.all()
    return render(request,'myapp/grades.html',{"grades":gradesList})

def students(request):
    stulist = Student.objects.all()
    context = {}
    context["students"] = stulist
    return render(request,'myapp/students.html', context)

def gradesStudents(request,num):
    grade = Grade.objects.get(pk=num)
    stulist = grade.student_set.all()
    context = {}
    context["students"] = stulist
    return render(request,'myapp/students.html', context)

from django.core.paginator import Paginator

def studentspage(request,pageid):
      allList = Student.objects.all()
      paginator = Paginator(allList, 6)
      page = paginator.page(pageid)

      return render(request,'myapp/studentspage.html',{"students":page})
