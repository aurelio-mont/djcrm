"""Website views."""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    """Home view"""

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
        return render(request, "home.html", {})


def logout_user(request):
    """Logout user view"""
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")
