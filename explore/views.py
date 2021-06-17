from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from scripts import search
from .models import Notification
from django.contrib import messages

# Create your views here.
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def searchview(request):
    if request.method == "POST":
        text = request.POST.get('search-for')
        if text:
            users = User.objects.all()
            result=search.search_for(users,text)

            return render(request, 'explore/search.html', {'results': result,'text':text})
        else:
            return render(request, 'explore/search.html')

    else:
        return render(request, 'explore/search.html')





def activityview(request):
    while(Notification.objects.all().count()>15):
        first=Notification.objects.first()
        Notification.delete(first)
    notification=Notification.objects.filter(notify_to=request.user)
    request_notify=[msg for msg in request.user.profile.follow_request.all() ]
    follow_back=[ user for user in request.user.profile.followers.all() ]
    follow_back=[ b for b in follow_back if not b  in request.user.profile.following.all() if  not request.user in b.profile.follow_request.all() ]
    return render(request, 'explore/activity.html',{'request_notifications':request_notify,'notifications':notification,'follow_back':follow_back})



def deletenotificationview(request,**kwargs):
    notification=Notification.objects.get(id=kwargs['pk'])
    Notification.delete(notification)
    return redirect('activity')

def requestview(request,**kwargs):
    user=User.objects.get(id=kwargs['pk'])
    if user.profile.public:
        user.profile.followers.add(request.user)
    else:
        user.profile.follow_request.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))




def requestacceptview(request,**kwargs):
    user=User.objects.get(id=kwargs['pk'])
    request.user.profile.follow_request.remove(user)
    request.user.profile.followers.add(user)
    user.profile.following.add(request.user)
    return redirect('activity')

def requestcancelview(request,**kwargs):
    user=User.objects.get(id=kwargs['pk'])
    request.user.profile.follow_request.remove(user)
    return redirect('activity')
