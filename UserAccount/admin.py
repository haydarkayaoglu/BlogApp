from django.contrib import admin
from UserAccount.models import UserData, BlogPost, BlogComment

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from UserAccount.models import UserProfile

admin.site.register(UserData)
admin.site.register(BlogPost)
admin.site.register(BlogComment)

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
