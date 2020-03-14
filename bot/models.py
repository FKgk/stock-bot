from django.db import models

# Create your models here.
class User(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	status = models.BooleanField(default=True)

class Issue(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=14)
	code = models.CharField(max_length=6)
