# Generated by Django 3.0 on 2022-03-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220331_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='count',
            field=models.CharField(default='', max_length=999999),
        ),
    ]