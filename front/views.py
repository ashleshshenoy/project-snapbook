from explore.models import Notification
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
from .models import Post, Comment
from explore.models import Notification
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages



# Create your views here.


def LikeView(request, **kwargs):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if request.user in post.like.all():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
        notification=Notification(notify_to=post.user,notify_from=request.user,notify_type='like')
        notification.save()
    return HttpResponseRedirect(reverse('post-detail', args=[kwargs['pk']]))





def about(request):
    return render(request, 'front/about.html')


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'front/home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user__in=[ usr for usr in self.request.user.profile.following.all()])
        return context
    



'''class PostListView(TemplateView):
    template_name='front/home.html'

    def get_context_data(self,**kwargs):
        context=super(PostListView,self).get_context_data(**kwargs)
        context['posts']=Post.objects.all()
        context['likes']=Like.objects.all()
        return context
'''


'''class PostDetailView(DetailView):
    model=Post

    def get_context_data(self,**kwargs):
        comments=Comment.objects.all()
        context=super(DetailView,self).get_context_data(**kwargs)
        context['comments']=comments
        return context'''




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'caption', 'location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image', 'caption', 'location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def PostDetailView(request, **kwargs):
    object = Post.objects.filter(id=kwargs['pk']).first()
    comment = Comment.objects.all()
    if request.method == 'POST':
        text = request.POST.get('comment-text')
        user = request.user
        post = Post.objects.filter(id=kwargs['pk']).first()
        instance = Comment(user=user, post=post, text=text)
        if text != '':
            instance.save()
        return HttpResponseRedirect(reverse('post-detail', args=[kwargs['pk']]))
    else:
        return render(request, 'front/post_detail.html', {'object': object, 'comments': comment})
