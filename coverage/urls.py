from django.urls import path
from coverage import views

app_name = 'coverage'

urlpatterns = [
    path('check/', views.check_view, name='check-coverage'),
]