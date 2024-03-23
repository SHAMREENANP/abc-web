from django.db import models

# Create your models here.
class item(models.Model):
    Name=models.TextField(max_length=255)
    price=models.TextField(max_length=255)
    orderno=models.IntegerField(null=True,blank=True)
    qunatity=models.IntegerField(null=True,blank=True)
    category=models.TextField(max_length=255,null=True,blank=True)
    description = models.TextField(max_length=220,null=True,blank=True)
    image=models.ImageField(upload_to="image/",null=True,blank=True) 