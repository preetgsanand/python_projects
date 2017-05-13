from __future__ import unicode_literals

from django.db import models

class Review(models.Model):
	username = models.CharField(max_length=100,blank=False)
	email = models.CharField(max_length=100,blank=False)
	added = models.DateTimeField(auto_now_add=True);
	content = models.TextField(max_length=1000,blank=False)

	def __unicode__(self):
		return self.username