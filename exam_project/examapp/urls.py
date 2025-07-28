"""
URL configuration for exam_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from examapp import views

# urlpatterns = [
#     path('', views.home, name='home'),
    
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.auth_page, name='auth_page'),        # ✅ This is the important one
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('verify/', views.verify_otp, name='verify_otp'),
#     path('logout/', views.logout_view, name='logout'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('send-otp/', views.request_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
]

