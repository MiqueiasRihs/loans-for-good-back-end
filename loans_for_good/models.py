from django.db import models

from loans_for_good.utils import MARITAL_STATUS_OPTIONS

class CustomerAnalysis(models.Model):
    class Meta:
        verbose_name = u'Análise de cliente'
        verbose_name_plural = u'Análise de clientes'
        
    name = models.CharField(max_length=200, verbose_name=u'Nome')
    document = models.CharField(max_length=15, verbose_name=u'Documento')
    email = models.CharField(max_length=200, verbose_name=u'Email', null=True, blank=True)
    aprroved = models.BooleanField(default=False, verbose_name='Aprovada?')
    marital_status = models.CharField(verbose_name=u'Estado civil', choices=MARITAL_STATUS_OPTIONS, max_length=50, null=True, blank=True)
    birth_date = models.DateField(auto_now_add=False, verbose_name='Data de nascimento', null=True, blank=True)
    nationality = models.CharField(max_length=100, verbose_name="Nacionalidade", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="Telefone", null=True, blank=True)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Renda mensal", null=True, blank=True)
