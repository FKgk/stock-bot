from django.db import models

# Create your models here.
class User(models.Models):
	id = models.CharField(primary_key=True, max_length=20)
	status = models.BooleanField(default=True)

class Issue(models.Models):
	id = models.CharField(primary_key=True, max_length=20)
	name = models.CharField(max_length=20)
	code = models.CharField(max_length=20)

