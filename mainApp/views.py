from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': [
        'Если у вас остались какие-то вопросы, то задавайте мне их по телефону',
        '(012)345-пошел-лесом'
    ]})
