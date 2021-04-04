from django.shortcuts import render
import random


# Create your views here.
def Home(request):
    return render(request, "generator/home.html")


def PasswordGenerator(request):
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    specials = "!@#$%^&*_+<>?;:"
    numbers = "0123456789"
    generated_password = ""
    password_length = int(request.GET.get('length'))

    pass_seed = lower_chars
    if request.GET.get('uppercase'):
        pass_seed += upper_chars
    if request.GET.get('special'):
        pass_seed += specials
    if request.GET.get('number'):
        pass_seed += numbers

    for i in range(password_length):
        generated_password += random.choice(list(pass_seed))

    return render(request, "generator/password.html", {"password": generated_password})
