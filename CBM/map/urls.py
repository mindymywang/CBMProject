from django.urls import path
from map import views

app_name='CBM_Map'

urlpatterns = [
    path('index/', views.index, name='index', kwargs = {"strName" : "mindy"}),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('businessDomainList/', views.businessDomainList, name="businessDomainList"),
    path('valuechain/', views.valuechain, name="valuechain"),
    path('processMap/', views.processMap, name="processMap"),
    path('getActivities/', views.getActivities, name="getActivities"),
]