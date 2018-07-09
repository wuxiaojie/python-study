# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Grade(models.Model):
      gname = models.CharField(max_length=20)
      gdate = models.DateTimeField()
      ggirlnum = models.IntegerField()
      gboynum = models.IntegerField()
      isDelete = models.BooleanField(default=False)
      def __str__(self):
         return ("%s,%s,%d,%d" % (self.gname, self.gdate, self.ggirlnum,self.gboynum))

class Student(models.Model):
      sname = models.CharField(max_length=20)
      sgender = models.BooleanField()
      sage = models.IntegerField()
      scontent = models.CharField(max_length=20)
      isDelete = models.BooleanField(default=False)
      sgrade = models.ForeignKey("Grade")
      def __str__(self):
         return ("%s,%s,%d,%s,%s" % (self.sname, self.sgender, self.sage, self.scontent, self.sgrade.gname))
