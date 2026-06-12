from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('/admin-dashboard/')
            return redirect('/')
        messages.error(request, 'Username atau password salah!')
    return render(request, 'core/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah dipakai!')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registrasi berhasil! Silakan login.')
            return redirect('/login/')
    return render(request, 'core/register.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')