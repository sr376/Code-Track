# Generated by Django 4.2.3 on 2023-09-13 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_notification_alter_profile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='streak',
        ),
    ]
