from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def say_hello(request):
    print('Debug has started and git has deleed')
    print('new brunch created')
    return render(request, 'hello.html', {'name': 'akash'})