from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from photologue.models import Photo, Gallery
from tagging.fields import TagField

class My_Photo(models.Model):
    pic     = models.ForeignKey(Photo, related_name='my_photo')    
    auth    = models.ForeignKey(User)

    def __unicode__(self):
        return pic.tittle

class My_Gallery(models.Model):
    gal = models.ForeignKey(Gallery, related_name='my_gallery') 
    photos = models.ManyToManyField(My_Photo, blank=True, null=True,
                                   related_name='categories')

    def __unicode__(self):
         return gal.tittle
