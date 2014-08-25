from django.conf.urls import patterns, include, url
from django.contrib import admin
from BlogApp import views
from UserAccount.views import users
from UserAccount.views import kullanici_ekle
from UserAccount.views import urlpath
from UserAccount.views import Arama
from UserAccount.views import userProfile
from BlogApp.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlogApp.views.home', name='home'),
    # url(r'^BlogApp/', include('BlogApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^users/', views.UserData_list),
    url(r'^posts/', views.Posts),
    url(r'adres-yolu/', urlpath),
    url(r'^arama/', Arama),
    url(r'^arama-form/', arama_form),
    url(r'^kullanici-ekle/', kullanici_ekle),

    url(r'accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}),
    url(r'^user-profil/', userProfile),


)



