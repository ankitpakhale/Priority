# Generated by Django 3.0 on 2022-03-31 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_problems_iscounted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problems',
            name='iscounted',
        ),
    ]
