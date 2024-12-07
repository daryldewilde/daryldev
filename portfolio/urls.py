from django.contrib import admin
from django.urls import path, include
from .views import portfolio_view, render_pdf_view, contact_me_view, ServiceWorkerView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_site'),
    path('', portfolio_view, name='portfolio'),
    path('download_resume/', render_pdf_view, name='download_resume'),
    path('contact_me/', contact_me_view, name='contact_me'),
    path('pwa/', include(('pwa.urls', 'pwa'), namespace='pwa')),
    path('serviceworker.js', ServiceWorkerView.as_view(), name='serviceworker'),
]
