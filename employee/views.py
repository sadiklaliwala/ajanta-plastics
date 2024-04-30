from django.shortcuts import render
from adminsite.models import Customer

# Create your views here.
def customershow(request):
    customer=Customer.objects.all()
    params ={'customer':customer}
    return render (request , "show_data/customershow.html",params)
