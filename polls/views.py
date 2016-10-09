from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
from .models import Content
from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html', {})
