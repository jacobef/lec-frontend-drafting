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

def parent_programs(request):
    return render(request, "parent_programs.html")

def admin_programs(request):
    return render(request, "admin_programs.html")

def students(request):
    return render(request, "student_roster.html")

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

def add_child(request):
    return render(request, "add_child.html")

def view_child(request):
    return render(request, "view_child.html")

def login(request):
    return render(request, "login.html")

def login_or_create(request):
    return render(request, "login_or_create.html")

def parent_view(request):
    return render(request, "parent_home.html")

def create_account(request):
    return render(request, "createAccount.html")

def standard_parent(request):
    return render(request, "standard_parent.html")

def edit_profile(request):
    return render(request, "edit_profile.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('parent_programs/', parent_programs),
    path('students/', students),
    path('community/', community),
    path('donors/', donors),
    path('messages/', messages),
    path('requests/', requests),
    path('calender/', calender),
    path('announcements/', announcements),
    path('children/', children),
    path('children/add_child/', add_child),
    path('children/view_child/', view_child),
    path('create_account/', create_account),
    path('login_or_create/', login_or_create),
    path('admin_programs/', admin_programs),
    path('', index),
    path('parent/', parent_view),
    path('standard_parent/', standard_parent),
    path('edit_profile/', edit_profile),
]
