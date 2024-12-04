from django.shortcuts import render


def platform(request):
    return render(request, 'third_task/platform.html')


def cart(request):
    return render(request, 'third_task/cart.html')


def cases(request):
    title = 'Наличие чехлов'
    text = 'Ассортимент чехлов'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/cases.html', context)
