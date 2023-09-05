from django import forms
from .models import user


class userForm(forms.ModelForm):
    class Meta:
        model=user
        fields='__all__'
        widgets={
            'Name': forms.TextInput(attrs={'class':'forms-control'}),
            'Email': forms.EmailInput(attrs={'class':'forms-control'}),
            'Password': forms.PasswordInput(attrs={'class':'forms-control'})
        }