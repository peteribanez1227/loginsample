# Generated by Django 3.0.6 on 2020-05-19 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_name', models.CharField(max_length=50)),
                ('incident_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Incident',
            },
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('datecreated', models.DateField()),
                ('profilepic', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupsInfo',
            fields=[
                ('userprofileinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testlogin.UserProfileInfo')),
                ('role', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
            ],
            bases=('testlogin.userprofileinfo',),
        ),
        migrations.CreateModel(
            name='UserDeletedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('datecreated', models.DateField()),
                ('datedeleted', models.DateField()),
                ('userdeletedfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testlogin.UserProfileInfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDeletedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_created', models.DateField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('empnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_created', models.DateField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('empnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='DisputeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispute_name', models.CharField(max_length=50)),
                ('dispute_type', models.CharField(max_length=50)),
                ('incident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testlogin.IncidentType')),
            ],
        ),
    ]
