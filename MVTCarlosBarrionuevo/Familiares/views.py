from django.shortcuts import render

from Familiares.models import Familiares

# Create your views here.
def familiares(request):
    familiares = Familiares.objects.all()

    context = {'familiares': familiares}
    
    return render(request,'familiares.html',context = context)