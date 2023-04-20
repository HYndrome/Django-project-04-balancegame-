from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
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
    

def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)


def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return redirect('posts:detail', post.pk)
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)