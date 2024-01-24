from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.signup_page, name='signup'),
    path('calculator', views.calculator, name='calculator'),
    path('edit/<int:result_id>/', views.edit_result, name='edit_result'),
    path('delete/<int:result_id>/', views.delete_result, name='delete_result'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout')
]