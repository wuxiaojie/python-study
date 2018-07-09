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
    url(r'^hello/$', view.hello),
    url(r"^haha/$", view.haha),
#    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
#    url(r'^$', view.hello),
    url(r'^search-post$', search2.search_post),
    url(r'^red1/$', view.redfun1),
    url(r'^main/$',view.main),
    url(r'^login/$',view.login),
    url(r"^quit/$",view.quit),
    url(r'^showmain/$',view.showmain),
    url(r'^marks/$',view.marks),
    url(r'^child/$',view.child),
    url(r'^upload/$',view.upload),
    url(r'^upload_dir/$',view.upload_dir),
    url(r'^request_arg/$',view.request_arg),
    url(r'^verifycode/$',view.verifycode),
    url(r'^verifycodefile/$',view.verifycodefile),
    url(r'^verifycodecheck/$',view.verifycodecheck),
    url(r'^myapp/', include("myapp.urls")),
    url(r"^.*$",view.index),
]
