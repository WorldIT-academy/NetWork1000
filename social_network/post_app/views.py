from django.shortcuts import render, redirect
from .models import Post,Tag
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os
from django.contrib.auth.decorators import login_required
from user_app.models import Profile
from .forms import PostForm


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request, "post_app/all_posts.html", context={"all_posts": all_posts})

# Декоратор перевіряє, чи злогінився користувач. Якщо користувач на залогнився - перенаправляє на сторінку авторизації
@login_required
def render_create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                image=form.cleaned_data['image'],
                author =Profile.objects.get(user= request.user), 
            )
            new_post.tags.set(form.cleaned_data['tags'])
            new_post.save()        
            return redirect('all_posts')
    else:
        form = PostForm()
    return render(request, 'post_app/create_post.html',context={'form':form})