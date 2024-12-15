from django import forms


class userForm(forms.Form):
    
    user_type=[
        ('student','Student'),
        ('instructure','Istructor')
    ]
    
    name = forms.CharField(label='Name',required=False,widget=forms.TextInput(attrs={'class':"form-control form-control-lg"}))
    email = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control form-control-lg"}))
    contact = forms.IntegerField(label='Name',widget=forms.TextInput(attrs={'class':"form-control form-control-lg"}))
    user= forms.CharField(label='User Type', widget=forms.Select(choices=user_type,attrs={'class':"form-control form-control-lg"}))

    # usertype = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control form-control-lg"}))
    