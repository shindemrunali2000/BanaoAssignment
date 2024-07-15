from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost, Category
from rest_framework import viewsets
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

@login_required
def create_blog_post(request):
    if request.user.profile.user_type != 'Doctor':
        return redirect('dashboard')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def doctor_blog_posts(request):
    if request.user.profile.user_type != 'Doctor':
        return redirect('dashboard')
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/doctor_blog_posts.html', {'blog_posts': blog_posts})

def blog_posts_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    blog_posts = BlogPost.objects.filter(category=category_name, draft=False)
    return render(request, 'blog/blog_posts_by_category.html', {'category': category, 'blog_posts': blog_posts})

from django.shortcuts import get_object_or_404

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog_detail.html', {'post': post})

@login_required
def patient_dashboard(request):
    profile = request.user.profile
    blog_posts = BlogPost.objects.filter(draft=False)
    return render(request, 'blog/patient_dashboard.html', {'profile': profile, 'blog_posts': blog_posts})