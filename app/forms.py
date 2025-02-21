from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields='__all__'
        widgets={
            'password':forms.PasswordInput(),
           're_password':forms.PasswordInput()
        }
    def clean(self):
        cleaned_data=super().clean()
        fpwd=cleaned_data.get('password')
        spwd=cleaned_data.get('re_password')
        if fpwd!=spwd:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
      