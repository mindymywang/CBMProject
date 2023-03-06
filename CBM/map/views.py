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
from .models import System_List
from .models import Rollout_Info
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
   vcMap = {}
   pcMap = {}
   slMap = {}
   rlMap = {}
   for bd in bdall:
       bdNo = bd.bd_no
       vcList = Value_Chain.objects.filter(bd_no=bdNo)
       vcMap[bdNo]=vcList
       for vc in vcList:
           vcNo = vc.vc_no
           pcList = Process_Chain.objects.filter(vc_no=vcNo)
           slList = System_List.objects.filter(vc_no=vcNo)
           slMap[vcNo]=slList
           for sl in slList:
               slno = sl.sl_no
               rlList = Rollout_Info.objects.filter(sl_no=slno)
               rlMap[slno]=rlList

           pcMap[vcNo]=pcList

   bdlist= {"bdlist":bdall,"vcMap":vcMap, "pcMap":pcMap, "slMap":slMap, "rlMap":rlMap}
   return render(request, "map/businessDomainList.html", context=bdlist)

def valuechain(request):
     selectedBdNo = request.GET.get('bdno')
     selectBD = Business_Domain.objects.get(bd_no=selectedBdNo)
     selectedVCListResult = Value_Chain.objects.filter(bd_no=selectedBdNo)
     selectedVCList = {"selectedVCList":selectedVCListResult,"selectBD":selectBD}
     return render(request,"map/value_chain.html",context=selectedVCList)


@register.filter(name='dict_get')
def dict_get(value, key):
    return value.get(key, '') 

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

def processMap(request):
     selectedPCNo = request.GET.get('vcno')
     selectedVC = Value_Chain.objects.get(vc_no = selectedPCNo)
     selectedPCResult =  Process_Chain.objects.filter(vc_no=selectedPCNo)
     selectedBDNo = selectedPCResult[0].bd_no
     selectBD = Business_Domain.objects.get(bd_no=selectedBDNo)
     cbmMap = {}
     pcMap = {}
     for selectedPC in selectedPCResult :
         selectedPCNo = selectedPC.pc_no
         selectedPCName = selectedPC.pc_name
         selectCBList = Component_Business.objects.filter(pc_no=selectedPCNo).order_by('cb_no')
         cbmMap[selectedPCNo] = selectCBList
         pcMap[selectedPCNo] = selectedPCName

     selectedPCList = {"selectedPCList":selectedPCResult, "cbmMap" : cbmMap, "pcMap" : pcMap, "selectedVCNo" :selectedPCNo, "selectBD": selectBD, "selectedVC":selectedVC}
     return render(request, "map/processMap.html",context=selectedPCList)

@csrf_exempt
def getActivities(request):    
    selectedCbno = request.POST.get('selectedCbno')
    response_data = {}
    response_data['calist'] = serializers.serialize("json",Component_Activity.objects.filter(cb_no=selectedCbno))
    return HttpResponse(json.dumps(response_data),content_type="application/json")



   
  