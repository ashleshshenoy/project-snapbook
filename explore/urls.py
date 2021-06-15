from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.searchview,name='search'),
    path('request/<int:pk>',views.requestview,name='follow-request'),
    path('request/<int:pk>/accept',views.requestacceptview,name='request-accept'),
    path('request/<int:pk>/cancel',views.requestcancelview,name='request-cancel'),
    path('activity/<int:pk>/delete',views.deletenotificationview,name='delete-activity'),
]
