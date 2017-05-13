from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Entity(models.Model):
	name = models.CharField(max_length=100,blank=False)
	phone = models.CharField(max_length=13,blank=False)
	email = models.EmailField()
	dob = models.DateTimeField(blank=False)
	added = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name

class Administrator(Entity):
	def __unicode__(self):
		return self.name

class Supervisor(Entity):
	supervisorAdmin = models.ForeignKey(Administrator, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.name

class Employee(Entity):
	employeeSupervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.name

class Job(models.Model):
	name = models.CharField(max_length=100,blank=False)
	added = models.DateTimeField(auto_now=False,auto_now_add=True)
	deadline = models.DateTimeField()
	jobemployee = models.ManyToManyField(Employee)
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