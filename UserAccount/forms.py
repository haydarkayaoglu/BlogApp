# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from UserAccount.models import BlogPost, UserProfile


class UserDataForm (ModelForm):

    class Meta:
        model = UserProfile

    def save(self, commit=True):
        instance = super(UserDataForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

    def clean_phone(self):
        tel = self.cleaned_data['phone']
        if tel != "":
            if len(tel) != 11:
                raise forms.ValidationError('Telefon numarasi 11 karakter olmalidir.')
        return tel


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "password1",
                  "password2",
                  "email")
        #exclude = ('username')



#kullanıcınn post göndermesi için
class UserPostCreationForm (forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content',)

    def save(self, commit=True):
        instance = super(UserPostCreationForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance


# class UserPostsForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost