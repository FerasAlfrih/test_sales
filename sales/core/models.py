from ast import mod
from http import client
from msilib.schema import Class
from django.db import models
from django.utils.translation import gettext_lazy as _


class Salesman(models.Model):
    slug = models.SlugField(_("Slug"), blank=True, null=True)
    name = models.CharField(_("Name"), max_length=50)
    percentage = models.IntegerField(_("Percentage"), default=10)

    class Meta:
        verbose_name = _("Salesman")
        verbose_name_plural = _("Salesmen")

    def __str__(self):
        return self.name

    def save(self):
        self.slug = self.name.replace(' ', '')
        super(Salesman, self).save()


class Client(models.Model):
    slug = models.SlugField(_("Slug"), blank=True, null=True)
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name

    def save(self):
        self.slug = self.name.replace(' ', '')
        super(Client, self).save()


class Book(models.Model):
    slug = models.SlugField(_("Slug"), blank=True, null=True)
    name = models.CharField(_("Name"), max_length=50)
    price = models.IntegerField(_("Price"))

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.name

    def save(self):
        self.slug = self.name.replace(' ', '')
        super(Book, self).save()


class Invoice(models.Model):
    client = models.ForeignKey("Client", verbose_name=_(
        "Client"), on_delete=models.PROTECT)
    salesman = models.ForeignKey("Salesman", verbose_name=_(
        "Salesman"), on_delete=models.PROTECT)
    book = models.ForeignKey("Book", verbose_name=_(
        "Book"), on_delete=models.PROTECT)
    date = models.DateField(_("Date"), auto_now=True,
                            auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self):
        return self.salesman.name
