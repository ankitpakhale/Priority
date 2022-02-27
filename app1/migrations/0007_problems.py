# Generated by Django 4.0.2 on 2022-02-27 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_delete_studentdata_remove_signup_isstu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(default='', max_length=30)),
                ('isappoved', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.signup')),
            ],
        ),
    ]
