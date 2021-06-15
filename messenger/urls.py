from django.urls import path
from . import views

urlpatterns = [
    path('',views.messengerhomeview,name='messenger-home')

]
