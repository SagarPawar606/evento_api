# Generated by Django 4.1.7 on 2023-02-19 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('profile_pic', models.ImageField(blank=True, default='default_avatar.jpg', upload_to='profile_pics', verbose_name='Profile Image')),
                ('is_publisher', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublisherAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Description will help others to know more about you/organization.', max_length=500, null=True)),
                ('location', models.CharField(max_length=100)),
                ('contact_details', models.CharField(help_text='You can mention contact number, email id or social handels here.', max_length=200, verbose_name='Contact Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='banner_images', verbose_name='Banner Image')),
                ('description', models.TextField(max_length=1000)),
                ('date_of_event', models.DateTimeField(verbose_name='Date of Event')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('venue', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('event_mode', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline/Live')], max_length=10)),
                ('event_monetized', models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], max_length=4)),
                ('event_cost', models.PositiveIntegerField()),
                ('no_of_seats', models.PositiveIntegerField(blank=True, null=True, verbose_name='No of seats')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.publisheraccount')),
            ],
        ),
    ]