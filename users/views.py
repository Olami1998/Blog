from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, User


# Create your views here.


def signup(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect('home:homeView')
        else:
            return redirect('home:aboutview')
    context = {
        "name":"lekzy",
        "gender":"male",
        "email":"abisolaolalekan19gmail.com",
        "form": UserCreationForm()
    }
    return render(request, 'accounts/django-register.html', context)



##def signup_view(request):# keep
    if request.user.is_authenticated:
        return redirect('home:homeView')

    return render(request, 'accounts/signup.html', {})



def login(request):
    return render(request, 'accounts/login.html')


def forgetpassword(request):
    return render(request, 'accounts/forgetpassword.html')