from django.shortcuts import render
import random


# Create your views here.

def today_dinner(request):
    foods = ['치킨','삼겹살','짜장면']
    context = {
        'foods' : random.choice(foods),
    }
    return render(request, 'today_dinner.html',context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    data = request.GET.get('message')
    context = {
        'data' : data,
    }
    return render(request,'catch.html',context)


def lotto_create(request):
    return render(request,'lotto_create.html')


def lotto(request):
    numbers = list(range(1,46))
    data = int(request.GET.get('message'))
    context = {
            'rdm' : [sorted(random.sample(numbers,6)) for _ in range(int(data))],
            'data' : data,
        }
    return render(request,'lotto.html',context)