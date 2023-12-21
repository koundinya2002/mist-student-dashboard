from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import login_form #, SignUpForm, EditProfileForm,
from django.contrib.auth.decorators import login_required


@login_required
def login_view(request):

    context = {}
    context['form'] = login_form

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/index/")
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect login credential(s)')
            return redirect("/")
        
    return render(request, "registration/login.html", {})



@login_required
def logout_view(request):
    logout(request)
    return  redirect("dashboard/home")