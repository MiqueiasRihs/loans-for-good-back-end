from django.db import models

from loans_for_good.utils import MARITAL_STATUS_OPTIONS, ANALYSIS_STATUS, \
    EnumAnalysisStatus, EnumMaritalStatusOptions

class CustomerAnalysis(models.Model):
    class Meta:
        verbose_name = u'Análise de cliente'
        verbose_name_plural = u'Análise de clientes'

    name = models.CharField(max_length=200, verbose_name=u'Nome')
    document = models.CharField(max_length=15, verbose_name=u'Documento')
    approved = models.BooleanField(default=False, verbose_name='Aprovada automaticamente?')
    analyzed_at = models.DateTimeField(auto_now_add=False, verbose_name='Análisada automaticamente em', null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name=u'Email', null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="Telefone", null=True, blank=True)
    nationality = models.CharField(max_length=100, verbose_name="Nacionalidade", null=True, blank=True)
    birth_date = models.DateField(auto_now_add=False, verbose_name='Data de nascimento', null=True, blank=True)
    status = models.SmallIntegerField(verbose_name=u'Status', choices=ANALYSIS_STATUS, default=EnumAnalysisStatus.DENIED)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Renda mensal", null=True, blank=True)
    marital_status = models.SmallIntegerField(verbose_name=u'Estado civil', choices=MARITAL_STATUS_OPTIONS, default=EnumMaritalStatusOptions.NONE)

    def __str__(self):
        return f'{self.name} - {self.document}'
    
    def save(self, *args, **kwargs):
        self.document = ''.join(filter(str.isdigit, self.document))
        
        super(CustomerAnalysis, self).save(*args, **kwargs)
    

class UserFormConfiguration(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Nome')
    field_settings = models.JSONField(default=dict)

    class Meta:
        verbose_name = u'Formulario de análise'
        verbose_name_plural = u'Formularios de análise'
    
    def __str__(self):
        return self.name
