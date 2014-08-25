# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response
from UserAccount.models import *
from django.template import RequestContext


def home(request):
    return HttpResponse("<h1>Ana Sayfa</h1>")


def UserData_list(request):
    users = UserData.objects.all()
    return render_to_response('UserData_list.html', locals())


def Posts(request):
    users = UserData.objects.all()
    posts = BlogPost.objects.all()
    comment = BlogComment.objects.all()
    data = UserData.objects.all()
    return render_to_response('Posts.html', locals())


#def arama(request):
#    if request.method == "GET":
#        kelime = request.GET['kelime']
#        return HttpResponse('<b>Aranan Kelime: </b> %s' % kelime)


def arama_form(request):
    return render_to_response('arama.html', context_instance=RequestContext(request))


def arama(request):
    if request.method == "POST":
        aranan = request.POST.get('aranan')
        return HttpResponse('Aranan ifade : %s' % aranan)
    else:
        return HttpResponse('Bu şekilde arama yapılamaz..')