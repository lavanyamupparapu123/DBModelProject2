from django.shortcuts import render
from DBModelapp2.models import Employee2
# Create your views here.
def empdata(request):
    emplist=Employee2.objects.all()
    dict1={'emplist':emplist}
    return render(request,'DBModelapp2/emp.html',context=dict1);
