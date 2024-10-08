# Generated by Django 4.2.3 on 2023-09-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_email_profile_email_verified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254),
        ),
    ]
