from django import forms


class userForm(forms.Form):
    name = forms.CharField()
    