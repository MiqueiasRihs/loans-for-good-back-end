from django.contrib import admin

from .models import CustomerAnalysis, UserFormConfiguration

from .forms import UserFormConfigurationForm

class CustomerAnalysisAdmin(admin.ModelAdmin):
    list_display = ('name', 'document', 'email', 'phone_number', 'approved',)
    search_fields = ('name', 'name', 'document', 'email',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'document', 'email', 'approved')
        }),
        ('Detalhes Pessoais', {
            'fields': ('marital_status', 'birth_date', 'nationality', 'phone_number', 'monthly_income')
        }),
    )
    
    list_filter = ('approved',)


class UserFormConfigurationAdmin(admin.ModelAdmin):
    form = UserFormConfigurationForm


admin.site.register(UserFormConfiguration, UserFormConfigurationAdmin)
admin.site.register(CustomerAnalysis, CustomerAnalysisAdmin)