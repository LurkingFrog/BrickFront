from django import forms
from django.forms import ValidationError

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=False)
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        required=False
    )

# auth_method tells which backend to use
# choices=['django', 'facebook', 'google']
    auth_method = forms.CharField(
        widget=forms.HiddenInput,
        label="Authentication Method",
        required=True,
    )
    token = forms.CharField(label="Social Token", required=False)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        self.fields['auth_method'].initial = 'django'
        self.user = None

    def clean(self):
        super(LoginForm, self).clean()

        if self.cleaned_data['auth_method'] == 'django':
            self._django()

        elif self.cleaned_data['auth_method'] == 'facebook':
            self._facebook()

        elif self.cleaned_data['auth_method'] == 'google':
            self._google()

        return self.cleaned_data

    def _django(self):
        data = self.cleaned_data
        if not all([data['username'], data['password']]):
            raise ValidationError(
                "Username and password are both required"
            )

        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user is not None:
            if user.is_active:
                self.user = user

            else:
                raise ValidationError(
                    "Your account is not active, please contact the site admin."
                )
        else:
            raise ValidationError(
                "Your username and/or password were incorrect."
            )
