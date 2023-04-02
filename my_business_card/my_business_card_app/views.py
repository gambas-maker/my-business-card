from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'my_business_card_app/index.html')

def other(request):
    return render(request, 'my_business_card_app/other.html')
