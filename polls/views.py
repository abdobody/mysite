from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

from .models import Content


def index(request):
    latest_title_list= Content.objects.order_by('-pub_date')[:5]
    context = { 'latest_title_list': latest_title_list}
    return render(request,'polls/index.html',context)
def detail(request, id):
    return HttpResponse ('y are looking at title %s' % id)
def result(request, id):
    response = "Youe are looking result f title %s."
    return HttpResponse(response % id)





