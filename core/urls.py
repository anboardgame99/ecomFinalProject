from django.urls import path
from core.views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = "home"

urlpatterns = [
    path("", index, name='index'),
    path('success', success, name='success'),
    path('contact', contact, name='contact'),
    path('tracking', tracking_order, name='tracking_order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
