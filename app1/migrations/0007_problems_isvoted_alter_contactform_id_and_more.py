# Generated by Django 4.0.1 on 2022-04-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_problems_iscounted'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='isvoted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='problems',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
