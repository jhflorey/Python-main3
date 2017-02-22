# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.
# class People(models.Model):
#       first_name = models.CharField(max_length=30)
#       last_name = models.CharField(max_length=30)
#       created_at = models.DateTimeField(auto_now_add=True)
#       updated_at = models.DateTimeField(auto_now=True)

# class Courses(models.Model):
# 	name = models.CharField(max_length=255)
# 	description = models.TextField()
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# many_to_one relationship 
from __future__import unicode_literals
from django.db import models
#create your models here:
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=UserManager()
	
class Post(models.Model):
	title = models.CharField(max_length=45)
	message = models.TextField(max_length=1000)
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




















