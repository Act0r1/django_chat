from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

# Create your views here.


def frontpage(req):
    return render(req, "core/frontpage.html")

# def logout(req):



def signup(req):
    if req.method == "POST":
        form = SignUpForm(req.POST)

        if form.is_valid():
            user = form.save()
            login(req, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(req, 'core/signup.html', {'form':form})