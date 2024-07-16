from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet


router = DefaultRouter()
router.register(r'blog_posts', BlogPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('doctor_posts/', views.doctor_blog_posts, name='doctor_blog_posts'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
   
]
