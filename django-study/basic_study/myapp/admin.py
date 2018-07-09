# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Grade,Student

# Register your models here.

class StudentInfo(admin.TabularInline):
      model = Student
      extra = 2

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):

      inlines = [StudentInfo]

      list_display = ["pk","gname","gdate","ggirlnum","gboynum","isDelete"]
      list_filter = ["gname"]
      search_fields = ["gname"]
      list_per_page = 5

#      fields = ["gname","gdate","ggirlnum","gboynum","isDelete"]
      fieldsets = [
                   ("num",  {"fields":["ggirlnum","gboynum"]}),
                   ("base", {"fields":["gname","gdate","isDelete"]})
      ]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
      def gender(self):
          if self.sgender:
             return "男"
          else:
             return "女"
      gender.short_description = "性别"
      list_display = ["pk","sname",gender,"sage","scontent","sgrade","isDelete"]
      list_filter = ["sname"]
      search_fields = ["sname"]
      list_per_page = 5


#admin.site.register(Grade,GradeAdmin)
#admin.site.register(Student,StudentAdmin)
#admin.site.register(Grade,Student)
