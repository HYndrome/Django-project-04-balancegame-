from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)
    if (request.user in post.select1_users.all()) or (request.user in post.select2_users.all()):
        return redirect('posts:detail', post_pk)
    else:
        if answer == 1:
            post.select1_users.add(request.user)
        elif answer == 2:
            post.select2_users.add(request.user)
        return redirect('posts:detail', post_pk)