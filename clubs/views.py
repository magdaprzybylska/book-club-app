from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, RegisterForm

# Create your views here.


def index(request):
    return render(request, "clubs/index.html")


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["f_name"],
                last_name=form.cleaned_data["l_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return render(
                request, "clubs/success.html", context={"username": user.username}
            )
    else:
        form = RegisterForm()
    return render(request, "clubs/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"], password=form.cleaned_data["password"]
            )
            if user is not None:
                return render(
                    request,
                    "clubs/success.html",
                    context={"username": form.cleaned_data["email"]},
                )
    form = LoginForm()
    return render(request, "clubs/login.html", {"form": form})


def user_logout(request):
    return render(request, "clubs/index.html")
