from django import forms
from django.contrib.auth.models import User
from loginapp.models import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('password','portfolio','picture')
class UserForm(forms.ModelForm):
    class Meta():
        model= User
        fields=('username','email')
