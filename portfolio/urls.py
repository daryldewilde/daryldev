from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('download_resume/', views.render_pdf_view, name='download_resume'),
]
