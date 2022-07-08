from multiprocessing import context
from django.shortcuts import render
from setuptools import PEP420PackageFinder

from blog.forms import CommentForm
from .models import Post, Category, Comment
# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')

    context = {'posts': posts, 'category': category}
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                description = form.cleaned_data["description"],
                post = post
            )
            comment.save()


    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comment': comment, 'form': form}
    return render(request, 'blog_detail.html', context)