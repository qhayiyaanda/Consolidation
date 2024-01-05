from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    Form for user registration.

    Inherits:
    - UserCreationForm: Django's built-in form for user creation with password confirmation.

    Attributes:
    - username (CharField): Field for the username with a maximum length of 50 characters.
    - first_name (CharField): Field for the user's first name with a maximum length of 50 characters.

    Meta:
    - model (User): Specifies the User model.
    - fields (tuple): Fields included in the form - 'username', 'password1', 'password2', 'first_name'.
    """

    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50) 

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name')


class LoginForm(forms.Form):
    """
    Form for user login.

    Attributes:
    - username (CharField): Field for entering the username.
    - password (CharField): Field for entering the password, with a widget for password input.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
