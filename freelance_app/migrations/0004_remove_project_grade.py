# Generated by Django 2.0 on 2020-01-21 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0003_auto_20200121_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Grade',
        ),
    ]
