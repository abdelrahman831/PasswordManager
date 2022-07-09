from django.db import models

# Create your models here.
class User_Registration(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    username = models.TextField(max_length=191)
    password = models.TextField(max_length=191)


class Password_Manager(models.Model):
    registered_user = models.TextField(default='none')
    siteName = models.TextField(max_length=191)
    userName = models.TextField(max_length=191)
    password = models.TextField(max_length=191)

class login_form(models.Model):
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=20)

