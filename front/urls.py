from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,LikeView
urlpatterns = [
    path('', PostListView.as_view(),name="front-page"),
    path('post/<int:pk>/',PostDetailView,name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('like/<int:pk>/',LikeView,name='post-like'),
    path('about/',views.about,name='about'),
]
