from django.contrib import admin
from map.models import Business_Domain
from map.models import Value_Chain
from map.models import Process_Chain

# Register your models here.

admin.site.register(Business_Domain)
admin.site.register(Value_Chain)
admin.site.register(Process_Chain)
