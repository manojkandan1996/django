# newsletter_project/urls.py

from django.contrib import admin
from django.urls import path
from newsletter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.subscribe_model_form, name='home'),  # ✅ corrected
    path('subscribe-model/', views.subscribe_model_form, name='subscribe-model'),
    path('subscribe-manual/', views.subscribe_manual_form, name='subscribe-manual'),
]