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

class Component_Activity(models.Model):
    ca_no = models.BigIntegerField(primary_key=True)
    ca_name = models.CharField(max_length=100, default=None, null=True)
    ca_eng_name = models.CharField(max_length=100, default=None, null=True)
    cb_no = models.BigIntegerField(default=None, null=True)
    pc_no = models.CharField(max_length=50, default=None, null=True)
    bd_no = models.CharField(max_length=20, default=None, null=True)
    vc_no = models.CharField(max_length=50, default=None, null=True)

class System_List(models.Model):
    sl_no = models.BigIntegerField(primary_key=True)
    system_name=models.CharField(max_length=200, default=None, null=True)
    system_eng_name=models.CharField(max_length=200, default=None, null=True)
    usecase_name=models.CharField(max_length=200, default=None, null=True)
    usecase_eng_name=models.CharField(max_length=200, default=None, null=True)
    flywheel_no = models.CharField(max_length=200, default=None, null=True)
    belong_platform = models.CharField(max_length=200, default=None, null=True)
    is_package = models.CharField(max_length=5,null=True,default=None)
    cb_no = models.BigIntegerField(default=None, null=True)
    pc_no = models.CharField(max_length=50, default=None, null=True)
    bd_no = models.CharField(max_length=20, default=None, null=True)
    vc_no = models.CharField(max_length=50, default=None, null=True)
    ca_no = models.BigIntegerField(default=None, null=True)

class  Rollout_Info(models.Model):
      ri_no =models.BigIntegerField(primary_key=True)
      plant_name=models.CharField(max_length=50,default=None,null=True)
      go_live_date = models.DateField(null=True)     
      current_use_status = models.CharField(max_length=10,default=None,null=True)
      sl_no = models.BigIntegerField(default=None, null=True)




