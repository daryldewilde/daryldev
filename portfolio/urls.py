from django.contrib import admin
from django.urls import path, include
from .views import portfolio_view, contact_me_view

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('contact_me/', contact_me_view, name='contact_me'),
]
