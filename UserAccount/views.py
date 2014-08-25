# -*- coding: utf-8 -*-
from django.core.context_processors import request

from django.http import *
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from UserAccount.models import *
from UserAccount.forms import UserDataForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.contrib.auth import authenticate, login


def Arama(request):
    if request.method == "GET":
        kelime = request.GET['kelime']
        return HttpResponse('<b>Aranan Kelime: </b> %s' % kelime)


def urlpath(request):
    urlpath = request.path
    return HttpResponse('<b>Adres Yolu: </b>%s' % urlpath)

@login_required
def users(request):
    return render_to_response('UserData_list.html', locals())


def userProfile(Request):
    if request.GET.get('cikis'):
        logout(request)
        return HttpResponseRedirect('/user-profil/')

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

    return render_to_response('UserProfile_giris.html', locals(), context_instance=RequestContext(request))
#    return render_to_response('UserProfile.html', locals())
#       if not request.user.is_authenticated():
 #           return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


def kullanici_kontrol(user):
    return "haydark" in user.username


@login_required
@user_passes_test(kullanici_kontrol)
def kullanici_ekle(request):
    if request.method == "POST":

        # adi = request.POST.get('adi')
        # soyadi = request.POST.get('soyadi')
        # telefon = request.POST.get('telefon')
        # eposta = request.POST.get('eposta')
        #
        # hatalar = []
        # if not (adi or soyadi):
        #     hatalar.append('Adı veya soyadı boş bırakılamaz.')
        # if eposta:
        #     if not ('@' and '.') in eposta:
        #         hatalar.append('Doğru bir E-posta adresi girmelisiniz.')
        # if telefon:
        #     if len(telefon) != 11:
        #         hatalar.append('Telefon numarası 11 haneli olmalı.')
        # if hatalar:
        #     return render_to_response('UserAccount/UserForm.html', locals(), context_instance=RequestContext(request))
        # else:
        form = UserDataForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print 'form valid'
            form.save()
            return 

        return render(request, 'UserForm.html', {"form": form})
    # return HttpResponseRedirect(reverse('polls:results', args=(p.id,))
    else:
        form = UserDataForm()
        return render(request, 'UserForm.html', {"form": form})
        #return render_to_response('UserForm.html', context_instance=RequestContext(request))


def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'Posts.html')
        else:
            # Return a 'disabled account' error message
            print'hesabınızın aktivasyonunu tamamlayınız'
    else:
        # Return an 'invalid login' error message.
        print 'giris basarisiz'
