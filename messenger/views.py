from datetime import date
from messenger.models import Message
from django.shortcuts import render

def messengerhomeview(request,**kwargs):
    
    data=Message.objects.filter(receiver=request.user)
    objects=set([ usr.sender for  usr in data])
    return render(request,'messenger/home.html',{'objects':objects})

