# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import ModelForm
from UserAccount.models import UserData
from django.contrib.auth.hashers import make_password


class UserDataForm (ModelForm):

    sifre = forms.CharField(label="Şifre", help_text="Bir parola yazın", required=False)

    class Meta:
        model = UserData
        fields = ('first_name', 'last_name', 'username', 'sifre', 'age', 'phone', 'email')

    def save(self, commit=True):
        instance = super(UserDataForm, self).save(commit=False)
        if self.cleaned_data.get('sifre'):
            instance.password = make_password(self.cleaned_data['sifre'])
        if commit:
            instance.save()
        return instance

    def clean_phone(self):
        tel = self.cleaned_data['phone']
        if tel != "":
            if len(tel) != 11:
                raise forms.ValidationError('Telefon numarasi 11 karakter olmalidir.')
        return tel

