from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader

@login_required
def index(request):
    users = User.objects.all()
    context = {
        'users': users
        }
    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))

@login_required
def employee(request):
    return render(request, 'employee.html')
    # return HttpResponseRedirect('employee')
    # t = loader.get_template('employee.html')
    # context = {}
    # return HttpResponse(t.render(context, request))

@login_required
def upload_employee(request):
    return render(request, 'uploademployee.html', {})
    # return HttpResponseRedirect('/uploademployee')

@login_required
def attendance(request):
    return render(request, 'attendance.html', {})
    # context ={}
    # template=loader.get_template('attendance.html')
    # return render(request, 'attendance',{})
    # return HttpResponseRedirect('/attendance')

def disputes(request):
    return render(request,'disputes.html',{})


def logout_request(request):
    logout(request)
    template = 'logout.html'
    messages.info(request, "Logged out sucessfully!")
    return render(request, template)
    return HttpResponseRedirect('login.html')



def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'index.html', {'forms': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        usrobj = User.objects.filter(email=email)
        usrobj = usrobj.last()
        if not usrobj:
            return redirect('login_view')
        uname = usrobj.username
        password = request.POST['password']
        user = authenticate(username=uname, password=password)
        if user is not None and user.is_authenticated:
            if user.is_superuser or user.is_staff:
                print(user)
                login(request, user)
                return redirect('manageuser')
            else:
                login(request, user)
                return redirect('index')
        else:
            return HttpResponse("Inactive account")
            return render(request, 'login.html',)

    return render(request, 'login.html')

# def check_admin(user):
#     return user.is_superuser

# @user_passes_test(check_admin)
def adminpage(request):
    return render(request, 'adminpage.html',{})

@login_required
def manageuser(request):
    userList = User.objects.all()
    context = {
            'users' : userList
        }
    template = loader.get_template('manageuser.html')

    return HttpResponse(template.render(context, request))


@login_required
def view_user(request):
    userList = User.objects.all()
    context = {
            'users' : userList
        }
    template = loader.get_template('viewuser.html')

    return HttpResponse(template.render(context, request))
