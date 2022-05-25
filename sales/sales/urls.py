from django.contrib import admin
from django.urls import path
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('new_salesman', newSalesman, name='newSalesman'),
    path('new_client', newClient, name='newClient'),
    path('new_book', newBook, name='newBook'),
    path('new_invoice', newInvoice, name='newInvoice'),

]
