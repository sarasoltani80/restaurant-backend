from django.shortcuts import render , redirect
from . forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.models import User
from foods.models import Wallet
#from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import get_object_or_404, render


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'] , cd['email'] , cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            wallet = Wallet(user=user)
            wallet.save()
            messages.success(request , 'user registered successfuly', 'success')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request , 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username = cd['username'] , password = cd['password'])
            #if user is validated show the user, if not show error message and user would be null
            if user is not None:
                login(request , user)
                messages.success(request , 'logged in successfully', 'success')
                return redirect('show')
            else:
                messages.error(request, 'username or password is wrong' , 'danger')
    else:
        form = UserLoginForm()
    return render(request , 'login.html' , {'form': form})

def user_logout(request):
    logout(request)
    return redirect('show')
