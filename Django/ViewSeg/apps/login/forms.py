from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input100','name': 'Usuario','type': 'text', 'placeholder': 'Usuário'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100','name': 'pass','type': 'password', 'placeholder': 'Senha'})
    )