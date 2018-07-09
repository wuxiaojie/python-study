from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^grades/(\d)+/$', views.gradesStudents),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^studentspage/(\d)+/$', views.studentspage),
    url(r'^ajaxstudents/$',views.ajaxstudents),
    url(r'^studentsinfo/$',views.studentsinfo),
#    url(r'grades/grades/(\d)+$', views.gradesStudents),
]
