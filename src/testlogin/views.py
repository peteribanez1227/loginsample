from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group, GroupManager, PermissionManager, UserManager
from django.contrib import messages
from django.template import loader
from .models import Employee, UserProfileInfo, GroupsInfo, UserDeletedFile
import csv, io
import codecs
import hashlib

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_agent(user):
    return user.groups.filter(name='Agent').exists()


def forgotpassword(request):
    return render(request, 'forgotpassword.html', {})

@login_required
def index(request):
    groups = request.user.groups.all()
    users = User.objects.all()
    context = {
        'groups': groups,
        'users': users,
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
@user_passes_test(is_manager)
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
            if user.is_superuser:
                print(user)
                login(request, user)
                return redirect('adminpage')
            else:
                print(user)
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'login.html',)

    return render(request, 'login.html')


# def check_admin(user):
#     return user.is_superuser

# @user_passes_test(check_admin)
def adminpage(request):
    return render(request, 'adminpage.html',{})

@login_required
def manageuser(request, pk=None):
    groups = Group.objects.all()
    userList = User.objects.all()

    # get_user = User.objects.get(pk=pk)
    # print(get_user)

    # def get_context_data(self, *args, **kwargs):
    #     context = super.get_context_data(**kwargs)
    #
    #     context['user'] = User.objects.all()
    #     context['filter'] = User(self.request.GET, queryset=User.objects.all())
    #     return context

    context = {
            'groups': groups,
            'users' : userList,
            # 'getuser': get_user,
        }
    template = loader.get_template('manageuser.html')

    return HttpResponse(template.render(context, request))




@login_required
def view_user(request, uid):
    user = User.objects.get(id=uid)

    context = {
            'users': user,
        }

    template = loader.get_template('viewuser.html')

    return HttpResponse(template.render(context, request))


@login_required
def delete_user(request,uid):
    user = User.objects.get(id=uid)
    if user:
        userdeleted = UserDeletedFile.objects.create(user_id=user.id, name=user.username,
                                                     first_name=user.first_name,last_name=user.last_name,
                                                     email=user.email, is_staff=user.is_staff, is_active=user.is_active,
                                                     last_login=user.last_login)
        userdeleted.save()
        user.delete()
    return redirect('manageuser')



@login_required
def uploadusers(request):
    if request.method == 'POST':
        files = request.FILES['userfile']

        if not files.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')

        if request.FILES.get('userfile'):
            data_set = files.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=','):
                usr, created = User.objects.update_or_create(
                                    is_superuser=column[1],
                                    username=column[2],
                                    first_name=column[3],
                                    last_name=column[4],
                                    email=column[5],
                                    is_staff=column[6],
                                    is_active=column[7],
                )
                group = Group.objects.get(name=column[8])
                usr.set_password(column[0])
                usr.groups.add(group)
                usr.save()

            # for username, password in User.objects.all():
            #     if authenticate(username=username, password=password) is None:
            #         print
            #         "Failed to authenticate user {!r}".format(username)


    context = {}
    return render(request, "uploadusers.html", context)

            # else:
            #     with open(os.path.join(settings.BASE_DIR, 'media', 'core', 'employees.csv')) as f:
            #         reader = csv.reader(f)
            #         for row in reader:
            #              User.objects.create(
            #                 username=str(row[0]),
            #                 is_superuser= str(row[1]),
            #                 password = str(row[2]),
            #                 first_name = str(row[3]),
            #                 last_name = str(row[4]),
            #                 email=str(row[5])
            #             )

        # group = UserManager.objects.create(id=id)
        # response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="employee.csv"'
        #
        # writer = csv.writer(response)
        # writer.writerow()
        # return response


@login_required
def creategroup(request):
    if request.method == 'POST':
        if request.POST.get('groupname'):

            group = request.POST.get('groupname')
            Group.objects.create(name=group)
            # GroupManager.objects.filter(id=id)
            #Usergroups.objects.create(user_id = , group_id =)

        return render(request,'creategroup.html')

    return render(request, 'creategroup.html')


# @login_required
# def createuser(request):
#     if request.method == 'POST':
#         if request.method == '':
