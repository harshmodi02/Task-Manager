# Generated by Django 3.0.5 on 2020-04-23 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200423_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]