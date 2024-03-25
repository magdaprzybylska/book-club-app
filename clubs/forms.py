from django import forms


class RegisterForm(forms.Form):
    f_name = forms.CharField(label="First Name", max_length=50)
    l_name = forms.CharField(label="Last Name", max_length=50)
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
