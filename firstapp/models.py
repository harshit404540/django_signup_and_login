from django.db import models

# Create your models here.
class Signup(models.Model):
	fname = models.CharField(max_length = 200)
	lname = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	date_time = models.DateTimeField()
	secret_key = models.CharField(max_length=200)