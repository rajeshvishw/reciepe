from django.db import models

class reciepe_model(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField()
    price = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    
#hit count model
class URLHitCount(models.Model):
    url = models.CharField(max_length=255, unique=True)
    hit_count = models.IntegerField(default=0)