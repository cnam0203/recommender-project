from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/home")
    return render(request, "authentication/login.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/home')
        else:
            return render(request, "authentication/login.html")

    return render(request, "authentication/login.html")

@login_required(login_url="/authentication/login")
def user_logout(request):
    logout(request)
    return redirect("/authentication/login")