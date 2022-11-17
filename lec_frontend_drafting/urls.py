"""lec_frontend_drafting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path

def index(request):
    return render(request, "index.html")

def programs(request):
    return render(request, "programs.html")

def students(request):
    return render(request, "students.html")

def community(request):
    return render(request, "community.html")

def donors(request):
    return render(request, "donors.html")

def messages(request):
    return render(request, "messages.html")

def requests(request):
    return render(request, "requests.html")

def calender(request):
    return render(request, "calender.html")

def announcements(request):
    return render(request, "announcements.html")

def children(request):
    return render(request, "children.html")

def login(request):
    return render(request, "login.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('programs/', programs),
    path('students/', students),
    path('community/', community),
    path('donors/', donors),
    path('messages/', messages),
    path('requests/', requests),
    path('calender/', calender),
    path('announcements/', announcements),
    path('children/', children),
    path('', index),
]
