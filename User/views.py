from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in - Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')
