from __future__ import unicode_literals

from django.db import models


class Role(models.Model):
	name = models.CharField(max_length=100,blank=False)
	def __unicode__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=100,blank=False)
	info = models.TextField(max_length=1000,blank=True)
	def __unicode__(self):
		return self.name

class Batch(models.Model):
	department = models.ForeignKey(Department,blank=False,null=False)
	year = models.IntegerField()
	shift = models.IntegerField(choices=((1, "Morning"),
                                        (2, "Evening")),
                                default=3)
	def __unicode__(self):
		return self.department.name+"-"+str(self.year)

class Block(models.Model):
	name = models.CharField(max_length=100,blank=False)
	lat = models.DecimalField(max_digits=8, decimal_places=5,blank=True,null=True)
	lng = models.DecimalField(max_digits=8, decimal_places=5,blank=True,null=True)

	def __unicode__(self):
		return self.name

class Entity(models.Model):
	name = models.CharField(max_length=100,blank=False)
	phone = models.CharField(max_length=13,blank=False)
	email = models.EmailField()
	dob = models.DateTimeField(blank=False)
	department = models.ForeignKey(Department,on_delete=models.CASCADE)
	role = models.ManyToManyField(Role,blank=False,null=False)
	subject = models.CharField(max_length=100,blank=True) 
	added = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name

class Room(models.Model):
	name = models.CharField(max_length=100,blank=False)
	block = models.ForeignKey(Block,on_delete=models.CASCADE)
	floor = models.CharField(max_length=100,blank=True)
	category = models.IntegerField(choices=((1, "Administration"),
                                        (2, "Lab"),
                                        (3, "Lecture")),
                                default=3)
	assisstant = models.ForeignKey(Entity,blank=True,null=True)

	def __unicode__(self):
		return self.name

class Period(models.Model):
	entity = models.ForeignKey(Entity,blank=False,null=False)
	room = models.ForeignKey(Room,blank=False,null=False)
	batch = models.ForeignKey(Batch,blank=False,null=False)
	category = models.IntegerField(choices=((1, "Lab"),
                                        (2, "Lecture"),
                                        (3, "Tutorial")),
                                default=3)
	weekday = models.IntegerField(choices=((1, "Monday"),
                                        (2, "Tuesday"),
                                        (3, "Wednesday"),
                                        (4, "Thursday"),
                                        (5, "Friday")),
                                default=1)
	start = models.TimeField(auto_now=True)
	end = models.TimeField(auto_now=True)

	def __unicode__(self):
		return self.entity.name+"-"+str(self.batch)