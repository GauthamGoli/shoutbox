from django.db import models

class Post(models.Model):
	message = models.CharField(max_length=200)
	datetime = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.message
