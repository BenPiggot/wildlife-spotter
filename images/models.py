from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
  image = models.ImageField()
  image_type = models.CharField(max_length=255)
  description = models.TextField(max_length=2500)
  capture_date = models.DateTimeField()
  upload_date = models.DateTimeField()
  location = models.CharField(max_length=255)
  latitude = models.FloatField()
  longitude = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
    
  def __str__(self):
      return 

  def __unicode__(self):
      return 
