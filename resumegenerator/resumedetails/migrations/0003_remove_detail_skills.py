# Generated by Django 4.2.4 on 2024-03-08 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumedetails', '0002_remove_educationdetails_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='skills',
        ),
    ]