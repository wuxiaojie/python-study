"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import view,search,search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r"^haha/$", views.haha),
#    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
#    url(r'^$', views.hello),
    url(r'^search-post$', search2.search_post),
    url(r'^red1/$', views.redfun1),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r"^quit/$",views.quit),
    url(r'^showmain/$',views.showmain),
    url(r'^marks/$',views.marks),
    url(r'^child/$',views.child),
    url(r'^request_arg/$',views.request_arg),
    url(r'^verifycode/$',views.verifycode),
    url(r'^verifycodefile/$',views.verifycodefile),
    url(r'^verifycodecheck/$',views.verifycodecheck),
]
