# Generated by Django 4.0.5 on 2022-06-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=191)),
                ('password', models.TextField(max_length=191)),
            ],
        ),
    ]
