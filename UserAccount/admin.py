from django.contrib import admin
from UserAccount.models import BlogPost, BlogComment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from UserAccount.models import UserProfile


admin.site.register(UserProfile)
admin.site.register(BlogPost)
admin.site.register(BlogComment)


# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

