from django.db import models
from django.conf import settings

# Create your models here.
class Users(models.Model):
	name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	access_token = models.TextField()

	def __str__(self):
		return self.name

