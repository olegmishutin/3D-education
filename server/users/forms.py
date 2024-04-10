from django.forms import ModelForm
from .models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
