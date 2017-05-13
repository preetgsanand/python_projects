from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.

class Article(models.Model):
	title =  models.CharField(max_length=200,blank=False)
	body = models.TextField(max_length=10000,blank=False)
	tags = models.CharField(max_length=200,blank=True)
	added = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	category = models.IntegerField(choices=((1, "Health"),
                                        (2, "Politics"),
                                        (3, "ENtertainment"),
                                        (4, "Finance"),
                                        (5, "Loans")),
                                default=1)
	visitors_count = models.BigIntegerField(default=0)
	photo = models.TextField(max_length=100,blank=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("articles:detail",kwargs={'id':self.id})


class Review(models.Model):
	username = models.CharField(max_length=100,blank=False)
	email = models.CharField(max_length=100,blank=False)
	added = models.DateTimeField(auto_now_add=True);
	content = models.TextField(max_length=1000,blank=False)

	def __unicode__(self):
		return self.username