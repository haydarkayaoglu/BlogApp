# -*- coding: utf-8 -*-
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os

# class UserData(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50, blank=True)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=15)
#     userData = User.ForeignKey(User)


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, related_name='UserProfile')

    picture = models.ImageField(upload_to="profile_pic")
    city = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    education = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True, null=True, verbose_name="Yaşınız")

    # Other fields here
    single = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Cats.")

    def __unicode__(self):
        return u'%s' % (self.user)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


#Bloguser ise post gönderebilir.Yani anonim kullanıcı post gönderemeyecek
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    blogUser = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return u'%s' % (self.title)


#Hesap anonimse de yorum yapabilecek. Kullanıcı Verisini UserData'dan çekeceğiz
class BlogComment(models.Model):
    comment = models.TextField(max_length=160, blank=True)
    blogPost = models.ForeignKey(BlogPost, related_name="comments")
    userProfile = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return u'%s' % (self.comment)

#
# def picturePath(instance, filename):
#     postfix = os.path.splitext(filename)[-1]
#     fileRegistryName = os.path.join('profilePictures', str(instance.user.id)+postfix)
#     return fileRegistryName







