from django.shortcuts import render, redirect
from django.contrib import messages
from front.models import Post, Comment
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username} you can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


"""view to handle profile visits :
counts the total no of posts on profile
counts total no of likes on profile
filters all the post made by profile
and parses it to the template
"""


@login_required
def profile_view(request, **kwargs):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    posts = Post.objects.filter(user=kwargs['pk'])

# count of total no of post made by the profile
    profileof = User.objects.filter(id=kwargs['pk']).first()
    total_post = Post.objects.filter(user=profileof).count()
# calculating total likes by iterating over all posts from profile
    total_like = 0
    posts = [i for i in Post.objects.filter(user=profileof)]
    for post in posts:
        total_like += post.like.count()
# caluclating the comments
    total_comment = 0
    comments = [i for i in Comment.objects.all()]
    for comment in comments:
        if comment.post.user == profileof:
            total_comment += 1

    no_of_post = len(Post.objects.filter(user=kwargs['pk']))
    parse = {'posts': posts, 'profileof': profileof, 'total_post': total_post,
             'total_like': total_like, 'total_comment': total_comment}
    return render(request, 'user/profileview.html', parse)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile is succesfully updated')
            return redirect('profile-view')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form,
               'p_form': p_form}
    return render(request, 'user/profile.html', context)


