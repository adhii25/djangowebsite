from django.http import HttpResponse
from django.shortcuts import render
from  . models import Place ,People
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

def pics(request):
    obj = People.objects.all()
    return render(request, "index.html", {'work': obj})
#def division(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #res=x/y
    #return render(request,"result.html",{'result':res})


