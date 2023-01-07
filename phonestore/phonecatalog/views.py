# Create your views here.
from django.http import HttpResponse
from .models import Phone, PhoneMake
from django.template import loader
from django.shortcuts import render,  get_object_or_404


def index(request):
    """View function for home page of site."""
    phone_list = Phone.objects.order_by('-launch_date')
    num_phones = Phone.objects.all().count()
    # template = loader.get_template('phonecatalog/index.html')
    context = {
        'phone_list': phone_list,
        'num_phones': num_phones,
    }
    return HttpResponse(render(request, 'phonecatalog/index.html', context))


def detail(request, phone_id):
    phone = get_object_or_404(Phone, pk=phone_id)
    return render(request, 'phonecatalog/detail.html', {'phone': phone})
