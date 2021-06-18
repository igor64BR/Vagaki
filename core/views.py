from django.shortcuts import render, get_object_or_404
from .forms import OfferForm, CandidateForm
from django.contrib import messages
from .models import Offer


def index(request):  # Redirect to the index page
    if str(request.user) != 'AnonymousUser':  # Registered user
        user = str(request.user).title()
        if request.user.is_superuser:  # Administrator user
            admin = True
        else:
            admin = False
    else:
        admin = False
        user = 'novo usuário'
    context = {
        'user': user,
        'admin': admin,
    }
    return render(request=request, context=context, template_name='index.html')


def job_offers(request):  # Redirect to the job offers table
    if request.user.is_superuser:
        admin = True
    else:
        admin = False
    context = {
        'offers': Offer.objects.all(),
        'admin': admin
    }
    return render(request=request, context=context, template_name='job_offers.html')


def new_offer(request):  # Redirect to a form create a new offer
    if request.user.is_anonymous:
        return render(request=request, template_name='index.html')
    if str(request.method) == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            form = OfferForm()
            messages.success(request=request, message='Oferta publicada com sucesso!')
        else:
            messages.error(request=request, message='Falha no envio')
    else:
        form = OfferForm()

    context = {
        'form': form
    }
    return render(request=request, context=context, template_name='new_offer.html')


def offer_redirect(request, pk):
    if str(request.method) == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            form = CandidateForm()
            messages.success(request=request, message='Oferta publicada com sucesso!')
        else:
            messages.error(request=request, message='Falha no envio')
    else:
        form = CandidateForm()

    offer = get_object_or_404(Offer, id=pk)
    context = {
        'offer': offer,
        'form': form
    }
    return render(request=request, template_name='redirect.html', context=context)


def register(request):
    context = {

    }
    return render(request=request, template_name='request.html', context=context)