from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import register
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Business_Domain
from .models import Value_Chain
from .models import Process_Chain
from .models import Component_Business
from .models import Component_Activity
import json



# Create your views here.
def index(request,strName):
     return HttpResponse(f"YoYo   {strName}")

def aboutus(request):
     return HttpResponse("關於我們")

def first(request):    
     return render(request, "map/first_page.html")

def businessDomainList(request):   
   bdall = Business_Domain.objects.all()
   bdlist= {"bdlist":bdall}
   return render(request, "map/businessDomainList.html", context=bdlist)

def valuechain(request):
     selectedBdNo = request.GET.get('bdno')
     selectedVCListResult = Value_Chain.objects.filter(bd_no=selectedBdNo)
     selectedVCList = {"selectedVCList":selectedVCListResult}
     return render(request,"map/value_chain.html",context=selectedVCList)


@register.filter(name='dict_get')
def dict_get(value, key):
    return value.get(key, '') 

def processMap(request):
     selectedPCNo = request.GET.get('vcno')
     selectedPCResult =  Process_Chain.objects.filter(vc_no=selectedPCNo)
     cbmMap = {}
     pcMap = {}
     for selectedPC in selectedPCResult :
         selectedPCNo = selectedPC.pc_no
         selectedPCName = selectedPC.pc_name
         selectCBList = Component_Business.objects.filter(pc_no=selectedPCNo).order_by('cb_no')
         cbmMap[selectedPCNo] = selectCBList
         pcMap[selectedPCNo] = selectedPCName

     selectedPCList = {"selectedPCList":selectedPCResult, "cbmMap" : cbmMap, "pcMap" : pcMap, "selectedVCNo" :selectedPCNo}
     return render(request, "map/processMap.html",context=selectedPCList)

@csrf_exempt
def getActivities(request):
    #bdall = Business_Domain.objects.all()
    
    selectedCbno = request.POST.get('selectedCbno')
    response_data = {}
    response_data['bdlist'] = serializers.serialize("json",Component_Activity.objects.filter(cb_no=selectedCbno))
    return HttpResponse(json.dumps(response_data),content_type="application/json")



   
  