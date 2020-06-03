from django.db import models, migrations
from django.db.models import Model
from django.contrib.auth.models import User, Group



class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    datecreated = models.DateField()
    profilepic = models.CharField(max_length=50)
    email = models.CharField(max_length=40)


class GroupsInfo(UserProfileInfo):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    empid = models.ForeignKey(Group, on_delete=models.CASCADE)
    empnum = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_created = models.DateField()

    class Meta:
        db_table = 'Employee'


class UserDeletedFile(models.Model):
    userdeletedfile = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    last_login = models.IntegerField()
    datecreated = models.DateField()


class EmployeeDeletedFile(models.Model):
    empid = models.ForeignKey(Group, on_delete=models.CASCADE)
    empnum = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_created = models.DateField()


class IncidentType(models.Model):
    incident_name = models.CharField(max_length=50)
    incident_type = models.CharField(max_length=50)

    class Meta:
        db_table = "Incident"

class DisputeInfo(models.Model):
    incident_id = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    dispute_name = models.CharField(max_length=50)
    dispute_type = models.CharField(max_length=50)

# class GroupInfo(models.Model):
#     group = models.ManyToManyField(Group, on_delete=models.CASCADE, null=False)
#
#     def __str__(self):
#         return self.user.group

# class EmployeeProfile(models.Model):
#     empid = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     empnum = models.IntegerField()
#     last_name = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     datecreated = models.DateField()
#
#     def __str__(self):
#         return f'{self.first_name}{self.last_name}'


