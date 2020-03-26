from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def index(request):
    return render(request, 'index.html',{})


# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out sucessfully!")
#     return redirect('')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = self.request.POST.get('password', None)
            authenticated = authenticate(
                username=user.username,
                password=password
            )
            if authenticated:
                login(request, authenticated)
                return redirect("homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
        form = UserCreationForm()
        return render(request, "register", context={"form":form})

def login_view(request):
    return render(request,'login.html',{})
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('')
        else:
            form = AuthenticationForm()
        return render(request,'404.html',{'form':form})