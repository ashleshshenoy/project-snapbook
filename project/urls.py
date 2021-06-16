"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_view
from django.contrib.auth import views as auth_views
from front import views as front_view
from explore import views as explore_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from  django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messenger/',include('messenger.urls')),
    path('front/', include("front.urls")),
    path('', include("front.urls")),
    path('explore/', include("explore.urls")),
    path('register/', user_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('activity/', explore_view.activityview, name='activity'),
    path('profile/<int:pk>/', user_view.profile_view, name='profile-view'),
    path('edit/', user_view.profile, name='profile-edit'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
