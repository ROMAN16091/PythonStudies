from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.book_list, name = 'book_list'),
    path('add/', views.add_book),
    path('edit/<int:pk>/', views.edit_book),
    path('delete/<int:pk>/', views.delete_book),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'catalog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout')
]