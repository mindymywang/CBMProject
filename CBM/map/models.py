from django.db import models

# Create your models here.

class Business_Domain(models.Model):
    bd_no = models.CharField(primary_key=True, max_length=20, default=None)
    bd_name = models.CharField(max_length=20, default = None)
    bd_eng_name = models.CharField(max_length=100, default=None)
  

class Value_Chain(models.Model):
    vc_no = models.CharField(primary_key=True,max_length=50, default=None)
    vc_name = models.CharField(max_length=100, default=None)
    vc_eng_name = models.CharField(max_length=100, default=None, null=False)
    bd_no = models.CharField(max_length=20, default=None)

class Process_Chain(models.Model):
    pc_no = models.CharField(primary_key=True,max_length=50, default=None)
    pc_name = models.CharField(max_length=100, default=None)
    pc_eng_name=models.CharField(max_length=100, default=None, null=False)
    bd_no = models.CharField(max_length=20, default=None)
    vc_no = models.CharField(max_length=50, default=None)

class Component_Business(models.Model):
    cb_no =models.BigIntegerField(primary_key=True)
    cb_name =  models.CharField(max_length=100, default=None, null=True)
    cb_eng_name =  models.CharField(max_length=100, default=None, null=True)
    cb_type = models.CharField(max_length=50, default=None, null=True)
    cb_eng_type = models.CharField(max_length=50, default=None, null=True)
    pc_no = models.CharField(max_length=50, default=None, null=True)
    bd_no = models.CharField(max_length=20, default=None, null=True)
    vc_no = models.CharField(max_length=50, default=None, null=True)