from django.conf.urls import patterns, include, url
from django.contrib import admin
from BlogApp import views

from UserAccount.views import users
from UserAccount.views import kullanici_ekle
from UserAccount.views import urlpath
from UserAccount.views import userProfile
from UserAccount.views import userLogin
from UserAccount.views import register
from UserAccount.views import profilegiris

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^users/', views.UserData_list),
    url(r'^posts/', views.Posts),
    url(r'adres-yolu/', urlpath),
    url(r'^kullanici-ekle/', kullanici_ekle),

    url(r'accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}),

     #url(r'^user-profile/', userProfile),
     #url(r'user-login/', userLogin),

     #url(r'profile/profilePictures/(.*)', 'UserAccount.views.profilePictures'),
    url(r'^register/', register),


    url(r'^UserProfile/', profilegiris),

)



