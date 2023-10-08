from django.db import models

#Create your models here.
class hotwheels(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    email_id = models.CharField(max_length=255)
    number = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class tomica(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    email_id = models.CharField(max_length=255)
    number = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class maisto(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    email_id = models.CharField(max_length=255)
    number = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class majorette(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    email_id = models.CharField(max_length=255)
    number = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class mathchbox(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    email_id = models.CharField(max_length=255)
    number = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class others(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    email_id = models.CharField(max_length=255)
    number = models.IntegerField()
    image_url = models.CharField(max_length=2083)

