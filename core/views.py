from django.shortcuts import render


def index(request):
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


def job_offers(request):
    context = {

    }
    return render(request=request, context=context, template_name='job_offers.html')


def admin_area(request):
    pass
