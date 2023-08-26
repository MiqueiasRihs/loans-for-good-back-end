# Generated by Django 4.2.4 on 2023-08-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('document', models.CharField(max_length=15, verbose_name='Documento')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('aprroved', models.BooleanField(default=False, verbose_name='Aprovada?')),
                ('marital_status', models.CharField(blank=True, choices=[(1, 'Solteiro'), (2, 'Casado'), (3, 'Divorciado'), (4, 'Viúvo')], max_length=50, null=True, verbose_name='Estado civil')),
                ('birth_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('nationality', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nacionalidade')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('monthly_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Renda mensal')),
            ],
            options={
                'verbose_name': 'Análise de cliente',
                'verbose_name_plural': 'Análise de clientes',
            },
        ),
    ]
