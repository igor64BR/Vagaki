from django.contrib import admin
from .models import Offer, Candidate

# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'requirements', 'min_education', 'created', 'modified')

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'application', 'sal_claim', 'formation', 'education', 'created', 'modified')
