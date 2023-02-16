from django.db import models

# Create your models here.

class Business_Domain(models.Model):
    bd_no = models.CharField(primary_key=True, max_length=20),
    bd_name = models.CharField(max_length=50, null=True),
    bd_eng_name = models.CharField(max_length=50)


