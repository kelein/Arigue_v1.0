from django.db import models

# Create your models here.

# Server Class
class Server(models.Model):
	hostname = models.CharField(max_length=50, unique=True)
	ipaddr = models.GenericIPAddressField(blank=False, null=False, unique=True)
	sysinfo = models.CharField(max_length=50)
	arch = models.CharField(max_length=50)
   	kernal = models.CharField(max_length=50) 	
	mem_total = models.IntegerField() 
	mem_free = models.IntegerField() 
