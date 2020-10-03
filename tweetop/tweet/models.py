from django.db import models

# Create your models here.

class UserData(models.Model):
	userId = models.CharField(max_length = 120)

	def __str__(self):
		return self.userId

class TweetData(models.Model):
	userId = models.ForeignKey(UserData, on_delete = models.CASCADE)
	tweet_text = models.TextField()
	created_date = models.DateField()
