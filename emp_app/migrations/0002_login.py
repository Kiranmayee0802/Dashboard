# Generated by Django 4.2.6 on 2023-10-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]