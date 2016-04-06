from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

# Create your views here.

def loginaccount(request):
    print '1111111111'
    template_name = "login_account.html"
    
    #return HttpResponse('hello world, index')
    return render_to_response('accounts/index.html')
