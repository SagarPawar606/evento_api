# Generated by Django 4.1.7 on 2023-02-19 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraccount_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='full_name',
        ),
    ]
