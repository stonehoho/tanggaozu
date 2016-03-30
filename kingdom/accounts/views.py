from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print '1111111111'
    return HttpResponse('hello world, index')
