from django.shortcuts import redirect, render
from .models import *
from .funcs import *


def home(request):
    if request.method == "POST" and request.POST.get('sales') != '-':
        sal = request.POST.get('sales')
        salesman = Salesman.objects.get(slug=sal)
        invoices = Invoice.objects.filter(salesman=salesman)
        sum = 0
        for invoice in invoices:
            sum += invoice.book.price
        total = percent(sum, salesman.percentage)
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


def newSalesman(request):
    if request.method == 'POST':
        salesman = Salesman(name=request.POST.get(
            'name'), percentage=request.POST.get('percent'))
        salesman.save()
        return redirect('home')
    return render(request, 'newSalesman.html')


def newBook(request):
    if request.method == 'POST':
        book = Book(name=request.POST.get(
            'name'), price=request.POST.get('price'))
        book.save()
        return redirect('home')
    return render(request, 'newBook.html')


def newClient(request):
    if request.method == 'POST':
        client = Client(name=request.POST.get('name'))
        client.save()
        return redirect('home')
    return render(request, 'newClient.html')


def newInvoice(request):
    if request.method == 'POST':
        client = Client.objects.get(slug=request.POST.get('client'))
        salesman = Salesman.objects.get(slug=request.POST.get('salesman'))
        book = Book.objects.get(slug=request.POST.get('book'))
        invoice = Invoice(client=client, book=book, salesman=salesman)
        invoice.save()
        return redirect('home')
    context = {
        'books': Book.objects.all(),
        'clients': Client.objects.all(),
        'salesmen': Salesman.objects.all()
    }
    return render(request, 'newInvoice.html', context)
