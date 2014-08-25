# -*- coding: utf-8 -*-
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# class UserData(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50, blank=True)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=15)
#     userData = User.ForeignKey(User)


class UserData(User):

    age = models.IntegerField(blank=True, verbose_name="Yaşınız", validators=[
        MaxValueValidator(89),
        MinValueValidator(18)
        ]
    )

    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon Numaranız")

    def __unicode__(self):
        return u'%s,%s,%s' % (self.first_name, self.last_name, self.email)

    class Meta:
        ordering = ['first_name']


#Bloguser ise post gönderebilir.Yani anonim kullanıcı post gönderemeyecek
class BlogPost(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=1000)
    blogUser = models.ForeignKey(UserData)

    def __unicode__(self):
        return u'%s' % (self.content)


#Hesap anonimse de yorum yapabilecek. Kullanıcı Verisini UserData'dan çekeceğiz
class BlogComment(models.Model):
    comment = models.TextField(max_length=160, blank=True)
    blogPost = models.ForeignKey(BlogPost, related_name="comments")
    userData = models.ForeignKey(UserData)

    def __unicode__(self):
        return u'%s' % (self.comment)


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Cats.")

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)
