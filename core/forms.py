from .models import Candidate, Offer
from django import forms


class OfferForm(forms.ModelForm):  # Form to register a new job offer

    class Meta:

        model = Offer
        fields = ['name', 'salary', 'requirements', 'min_education']


class CandidateForm(forms.ModelForm):  # Form to register a candidature

    class Meta:
        model = Candidate
        fields = ['name', 'surname', 'email', 'phone', 'sal_claim', 'formation', 'education', 'application']
