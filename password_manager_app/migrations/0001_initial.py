# Generated by Django 4.0.5 on 2022-06-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.TextField(max_length=191)),
                ('userName', models.TextField(max_length=191)),
                ('password', models.TextField(max_length=191)),
            ],
        ),
    ]
