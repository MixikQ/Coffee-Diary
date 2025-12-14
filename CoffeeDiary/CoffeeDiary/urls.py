"""
URL configuration for CoffeeDiary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from coffee import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('u/<int:id>/', views.profile, name='userpage'),
    path('u/<int:id>/edit/', views.edit_profile, name='edit-user'),
    path('p/<int:id>/', views.postpage, name='postpage'),
    path('p/create/', views.create_post, name='create-post'),
    path('p/<int:id>/edit/', views.edit_post, name='edit-post'),
    path('p/<int:id>/delete/', views.delete_post, name='delete-post'),
]
