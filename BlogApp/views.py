# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response
from UserAccount.models import *


def home(request):
    return HttpResponse("<h1>Ana Sayfa</h1>")


def UserData_list(request):
    users = UserProfile.objects.all()
    return render_to_response('UserData_list.html', locals())


def Posts(request):
    users = UserProfile.objects.all()
    posts = BlogPost.objects.all()
    comment = BlogComment.objects.all()
    data = UserProfile.objects.all()
    return render_to_response('Posts.html', locals())




