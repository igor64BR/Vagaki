from django.urls import path
from .views import index, job_offers, admin_area

urlpatterns = [
    path('', index),
    path('job-offers', job_offers, name='job-offers'),
    path('admin-area', admin_area, name='admin-area')
]