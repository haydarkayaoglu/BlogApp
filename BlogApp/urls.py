from django.conf.urls import patterns, include, url
from django.contrib import admin
from BlogApp import views


from UserAccount.views import createUserPost, userProfile

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^users/', views.UserData_list),
    url(r'^posts/', views.Posts),



    url(r'accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}),

    url(r'accounts/password/$',
        'django.contrib.auth.views.password_change',
        name="password_change"),

    url(r'accounts/change-password-done/$',
        'django.contrib.auth.views.password_change_done',
        name="password_change_done"),

    url(r'^register/', 'UserAccount.views.register'),

    url(r'^createpost/', createUserPost),

    url(r'^UserProfile/', userProfile),

    #url(r'^editProfile/', 'UserAccount.views.EditProfile'),

)



