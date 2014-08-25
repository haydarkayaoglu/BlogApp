from django import forms


class bPosts(forms.Form):
    bcontent = forms.CharField(label='Post', max_length=300)
