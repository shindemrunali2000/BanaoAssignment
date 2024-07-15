from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from django.conf import settings
# from django.conf.urls import static

urlpatterns = [
    path('', views.home_page, name='home_page.html'),
    path('register/', views.register, name='register.html'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),

]

#  if settings.DEBUG:
    #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
