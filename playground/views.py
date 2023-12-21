from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def say_hello(request):
    print('Debug has started and git has deleed')
    print('Git added in this project and initilaize now')
    return render(request, 'hello.html', {'name': 'akash'})