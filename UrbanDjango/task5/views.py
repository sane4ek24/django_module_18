from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse


def sign_up_by_html(request):
    users = ['Oleg', 'Viktor', 'Sergey']
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'

        elif username in users:
            info['error'] = 'Пользователь с таким логином существует'

        else:
            return HttpResponse(f'Приветствуем, {username}')

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    users = ['Oleg', 'Viktor', 'Sergey']
    info = {}
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return HttpResponse(f'Приветствуем, {username}!')

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

