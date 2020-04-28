from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    # username = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    empnum = models.IntegerField()
    lname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    datecreated = models.DateField()

    def __str__(self):
        return self.empnum

# class AttendanceProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dateattended = models.OneToOneField(User, on_delete=models.CASCADE)
#
    
