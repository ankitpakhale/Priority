# Generated by Django 4.0.2 on 2022-02-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20220227_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
