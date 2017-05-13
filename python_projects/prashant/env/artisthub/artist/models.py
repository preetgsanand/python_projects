from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=100,blank=False)
	born = models.DateTimeField(blank=True)
	nationality = models.CharField(max_length=100,blank=True)
	work = models.TextField(max_length=5000,blank=True)
	awards = models.TextField(max_length=5000,blank=True)
	contact = models.CharField(max_length=20,blank=True)
	popularity = models.SmallIntegerField()

	added = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100,blank=False)
	email = models.EmailField()
	born = models.DateTimeField(blank=True)
	phone = models.CharField(max_length=100,blank=False)

	added = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.name