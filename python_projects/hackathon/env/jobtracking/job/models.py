from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	name = models.CharField(max_length=100,blank=False)
	phone = models.CharField(max_length=13,blank=False)
	email = models.EmailField()
	dob = models.DateTimeField(blank=False)
	department = models.IntegerField(choices=((1, "School Education & Literacy"),
                                        (2, "Higher Education"),
                                        (3, "States/UTS")),
                                default=1)
	role = models.IntegerField(choices=((1, "Admin"),
                                        (2, "User")),
                                default=1)
	job_count = models.IntegerField(default=0)
	attendance = models.IntegerField(choices=((1, "Absent"),
                                        (2, "Present")),
                                default=2)
	skills = models.CharField(max_length=200,blank=False,default="None")
	added = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.name

class Job(models.Model):
	name = models.CharField(max_length=100,blank=False)
	added = models.DateTimeField(auto_now=False,auto_now_add=True)
	deadline = models.DateTimeField()
	user = models.ManyToManyField(User,blank=True,null=True)
	userRequired = models.IntegerField(default=1)
	description = models.TextField(max_length=1000,blank=False,default='Please Add Description')
	department = models.IntegerField(choices=((1, "School Education & Literacy"),
                                        (2, "Higher Education"),
                                        (3, "States/UTS")),
                                default=1)
	status = models.IntegerField(choices=((1, "Abandoned"),
                                        (2, "Completed"),
                                        (3, "Ongoing")),
                                default=3)
	skills = models.CharField(max_length=200,blank=False,default="None")
	difficulty = models.IntegerField(default=1,blank=True)

	submitrequest = models.IntegerField(choices=((1, "On"),
                                        (2, "Off")),
                                default=2)
	def __unicode__(self):
		return self.name


class Part(models.Model):
	name = models.CharField(max_length=100,blank=False)
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	index = models.IntegerField()
	added = models.DateTimeField(auto_now=False,auto_now_add=True)
	deadline = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class Report(models.Model):
	title = models.CharField(max_length=100,blank=False)
	sender = models.ForeignKey(User)
	reportType = models.IntegerField(choices=((1, "Public"),
                                        (2, "Private")),
                                default=2)
	reciever = models.ForeignKey(User,null=True,blank=True,related_name="reciever")
	subject = models.CharField(max_length=200,blank=True)
	content = models.TextField(max_length=5000)
	added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title
