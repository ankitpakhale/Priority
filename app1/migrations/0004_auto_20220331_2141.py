# Generated by Django 3.0 on 2022-03-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20220331_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
