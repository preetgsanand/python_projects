from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100,blank=False)
	phone = models.CharField(max_length=13,blank=False)
	email = models.EmailField()
	address = models.CharField(max_length=200,blank=True)
	facebook = models.CharField(max_length=100,blank=True)
	instagram = models.CharField(max_length=100,blank=True)
	added = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name