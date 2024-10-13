"""Website views."""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.forms import SingUpForm
from website.models import Record


def home(request):
    """Home view"""

    records = Record.objects.all()

    # Check to see if logged in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("home")
        else:
            messages.error(
                request, "There was an error with your login, please try again"
            )
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def logout_user(request):
    """Logout user view"""
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    """Register user view"""

    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect("home")
    else:
        form = SingUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    """Customer record view"""

    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.error(request, "There was an error with your login, please try again")
        return redirect("home")
