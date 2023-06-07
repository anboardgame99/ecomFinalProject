from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path('register/', views.resgister_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]
