from django.db import models


class Intersection(models.Model):
	name = models.CharField(max_length=200)
	location= models.CharField(max_length=200)
	accidents = models.IntegerField()
	
# Create your models here.
