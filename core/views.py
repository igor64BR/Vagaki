from django.shortcuts import render
from .forms import OfferForm, CandidateForm
from django.contrib import messages


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
    context = {

    }
    return render(request=request, context=context, template_name='job_offers.html')


def new_offer(request):  # Redirect to a form create a new offer
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
