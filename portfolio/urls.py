from django.urls import path
from .views import portfolio_view, render_pdf_view, contact_me_view

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('download_resume/', render_pdf_view, name='download_resume'),
    path('contact_me/', contact_me_view, name='contact_me'),
]
