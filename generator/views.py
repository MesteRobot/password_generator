from django.shortcuts import render
import random


# Create your views here.
def Home(request):
    return render(request, "generator/home.html")


def PasswordGenerator(request):
    lower_chars = list("abcdefghijklmnopqrstuvwxyz")
    upper_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    specials = list("!@#$%^&*_+<>?;:")
    numbers = list("0123456789")
    generated_password = ""
    
    for i in range(10):
        generated_password += random.choice(lower_chars)

    return render(request, "generator/password.html", {"password": generated_password})
