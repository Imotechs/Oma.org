from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email','username','password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args,**kwargs)
        for fieldname in ['email','username','password1', 'password2']:
            self.fields[fieldname].help_text = None