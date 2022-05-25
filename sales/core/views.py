from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    if request.method == "POST" and request.POST.get('sales') != '-':
        sal = request.POST.get('sales')
        salesman = Salesman.objects.get(slug=sal)
        invoices = Invoice.objects.filter(salesman=salesman)
        sum = 0
        for invoice in invoices:
            sum += invoice.book.price
        total = sum / salesman.percentage
        context = {
            'invoices': invoices,
            "total": total,
            'sum': sum,
            'Salesman': salesman,
            'salesmen': Salesman.objects.all(),
        }
    else:
        context = {
            'salesmen': Salesman.objects.all()
        }
    return render(request, 'base.html', context)
