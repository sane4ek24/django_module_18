from django.shortcuts import render

def platform(request):
    return render(request, 'fourth_task/platform.html')


def cart(request):
    return render(request, 'fourth_task/cart.html')


def cases(request):
    title = 'Наличие чехлов'
    text = 'Ассортимент чехлов'
    cases_list = {'case': ['Pitaka for 15 Pro Max', 'Uniq for 15 Pro Max', 'Leather case for 15 Pro Max']}

    context = {
        'title': title,
        'text': text,
        'cases_list': cases_list
    }
    return render(request, 'fourth_task/cases.html', context)

