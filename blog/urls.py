from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, blog_detail
from .views import patient_dashboard

router = DefaultRouter()
router.register(r'blog_posts', BlogPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('doctor_posts/', views.doctor_blog_posts, name='doctor_blog_posts'),
    path('category/<str:category_name>/', views.blog_posts_by_category, name='blog_posts_by_category'),
    # path('category/', views.blog_posts_by_category, name='blog_posts_by_category'),
    path('dashboard/patient/', patient_dashboard, name='patient_dashboard'),
    path('post/<int:id>/', blog_detail, name='blog_detail'),
]
