# Create your views here.
from django.http import HttpResponse
from .models import Phone, PhoneMake
from django.template import loader
from django.shortcuts import render,  get_object_or_404


def index(request):
    """View function for home page of site."""
    phone_list = Phone.objects.order_by('-launch_date')
    template = loader.get_template('phonecatalog/index.html')
    # return HttpResponse(phone_list)
    context = {
        'phone_list': phone_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, phone_id):
    phone = get_object_or_404(Phone, pk=phone_id)
    return render(request, 'phonecatalog/detail.html', {'phone': phone})
