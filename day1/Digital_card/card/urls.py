from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_card, name='business_card'),
]
