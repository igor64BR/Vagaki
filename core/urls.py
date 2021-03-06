from django.urls import path
from .views import index, job_offers, new_offer, offer_redirect, register

urlpatterns = [
    path('new_offer', new_offer, name='new_offer'),  # Only admins
    path('', index, name='index'),
    path('job-offers', job_offers, name='job-offers'),  # Table with the offers avaliable
    path('redirect/<int:pk>', offer_redirect, name='redirect'),
    path('register/<int:pk>', register, name='register')
]
