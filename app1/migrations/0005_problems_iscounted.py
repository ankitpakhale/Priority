# Generated by Django 3.0 on 2022-03-31 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20220331_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='iscounted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
