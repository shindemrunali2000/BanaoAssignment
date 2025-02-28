from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm
from blog.models import BlogPost
from django.contrib.auth.models import User
from blog.views import create_blog_post
from appointment.views import doctor_list, book_appointment, appointment_detail

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        # form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User Registerd Successfully!")
            login(request, user)
            # return redirect('dashboard')
            return render(request, 'users/register.html', {'form': form})
    else:
        print("User Registerd Successfully!")
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.profile
    if profile.user_type == 'Patient':
        doctors = User.objects.filter(profile__user_type='doctor')
        blog_posts = BlogPost.objects.filter(draft=False)
        return render(request, 'users/patient_dashboard.html', {'profile': profile, 'blog_posts': blog_posts, 'doctors': doctors})
    elif profile.user_type == 'Doctor':
        # blog_posts = BlogPost.objects.filter(draft=True)
        blog_posts = BlogPost.objects.all()
        return render(request, 'users/doctor_dashboard.html', {'profile': profile, 'blog_posts': blog_posts})

def home_page(request):
    return render(request, 'users/home_page.html')



