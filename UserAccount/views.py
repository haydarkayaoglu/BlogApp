# -*- coding: utf-8 -*-
from django.core.context_processors import request
from django.contrib.auth.decorators import login_required

from django.http import *
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from UserAccount.models import *
from UserAccount.forms import UserDataForm, UserPostCreationForm
from UserAccount.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from models import UserProfile, BlogPost


def urlpath(request):
    urlpath = request.path
    return HttpResponse('<b>Adres Yolu: </b>%s' % urlpath)


@login_required
def users(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    return render_to_response('UserData_list.html', locals())


def user_profile(Request):
    if request.GET.get('cikis'):
        logout(request)
        return HttpResponseRedirect('/posts/')

    if request.POST.get('giris'):
        giris_formu = AuthenticationForm(data=request.POST)
        if giris_formu.is_valid():
            kullaniciadi = request.POST['username']
            sifre = request.POST['password']
            kullanici = authenticate(username=kullaniciadi, password=sifre)
            if kullanici is not None:
                if kullanici.is_active:
                    login(request, kullanici)
    else:
        giris_formu = AuthenticationForm()

    return render_to_response('UserProfile.html', locals(), context_instance=RequestContext(request))


def kullanici_kontrol(user):
    return "haydark" in user.username


@login_required
@user_passes_test(kullanici_kontrol)
def kullanici_ekle(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            print 'form valid'
            form.save()
        return render(request, 'UserForm.html', {"form": form})
    else:
        form = UserDataForm()
        return render(request, 'UserForm.html', {"form": form})


def userProfile(request):

    if not UserProfile.objects.filter(user=request.user.id):
        UserProfile.objects.create(user=request.user)

    if request.method == "POST":
        form = UserDataForm(request.POST, request.FILES, instance=request.user.UserProfile)
        if form.is_valid():
            form.save()
            #geçici olarak Posts a gönderdik
            return HttpResponseRedirect('/Posts/')
    else:
        form = UserProfileForm(instance=request.user.UserProfile)

    return render(request, 'UserProfile.html', {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #geçici
            #hem user hem de UserData'ya kaydetmeli
            usr = authenticate(username=form.cleaned_data['username'],
                               password=form.cleaned_data['password1'])
            if usr.is_authenticated():
                login(request, usr)
            return HttpResponseRedirect('/UserProfile/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html', locals(), context_instance=RequestContext(request))


def profile_pictures(request, picture_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'profile_pictures', picture_name)
    if os.path.join(file_path):
        picture = os.path.join(settings.MEDIA_ROOT, 'profile_pictures', picture_name)
        postfix = os.path.splitext(picture_name)[-1][1:]
        mimeTYPE = 'image/%s' % postfix
        picture_info = open(picture, "rb").read()
        return HttpResponse(picture_info, mimetype=mimeTYPE)
    else:
        picture_info = open(os.path.join(settings.MEDIA_ROOT, 'resim_yok.png'),"rb").read()
        return HttpResponse(picture_info, mimetype='image/png')


def createUserPost(request):
    #if not UserProfile.objects.filter(user=request.user.id):
    #    UserProfile.objects.create(user=request.user)

    if request.method == "POST":
        form2 = UserPostCreationForm(request.POST)
        if form2.is_valid():
            form2.instance.blogUser = request.user.UserProfile
            form2.save()
            #geçici olarak Posts a gönderdik
            return HttpResponseRedirect('/posts/')
    else:
        form2 = UserPostCreationForm()
    return render(request, 'createpost.html', {'form2':form2})