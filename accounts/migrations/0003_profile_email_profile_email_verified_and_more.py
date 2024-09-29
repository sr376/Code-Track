# Generated by Django 4.2.3 on 2023-08-31 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='xy@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='email_verified',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(default='Not Available', max_length=100),
        ),
    ]
