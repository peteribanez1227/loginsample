from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def index(request):
    return render(request, 'index.html',{})

def employee(request):
    return render(request, 'employee.html',{})

def upload_employee(request):
    return render(request, 'uploademployee.html',{})
    # return HttpResponseRedirect('/uploademployee')

def attendance(request):
    return render(request, 'attendance.html',{})
    # return HttpResponseRedirect('/attendance')
    # return redirect(request, 'attendance.html',{})

def disputes(request):
    return render(request,'disputes.html',{})

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
                return redirect('')
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
    form = UserCreationForm()
    args = {'form': form}
    return render(request, 'register.html', args)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect(request,'',next)
        else:
            form = AuthenticationForm()
        return render(request,'404.html',{'form':form})
    return render(request, 'login.html', {})
