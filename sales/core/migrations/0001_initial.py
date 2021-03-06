# Generated by Django 4.0.4 on 2022-05-25 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='salesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('percentage', models.IntegerField(default=10, verbose_name='Percentage')),
            ],
            options={
                'verbose_name': 'Salesman',
                'verbose_name_plural': 'Salesmen',
            },
        ),
        migrations.CreateModel(
            name='relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.book', verbose_name='Book')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.invoice', verbose_name='Invoice')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='books',
            field=models.ManyToManyField(through='core.relation', to='core.book', verbose_name='Books'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.client', verbose_name='Client'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.salesman', verbose_name='Salesman'),
        ),
    ]
