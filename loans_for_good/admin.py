from django.contrib import admin

from .models import CustomerAnalysis, UserFormConfiguration

from .forms import UserFormConfigurationForm

class CustomerAnalysisAdmin(admin.ModelAdmin):
    list_display = ('name', 'document', 'email', 'phone_number', 'approved', 'status', 'analyzed_at',)
    search_fields = ('name', 'name', 'document', 'email',)
    readonly_fields = ['analyzed_at', 'approved']
    
    fieldsets = (
        ('Situação', {
            'fields': ('status',)
        }),
        ('Informações Básicas', {
            'fields': ('name', 'document', 'email', 'approved', 'analyzed_at')
        }),
        ('Detalhes Pessoais', {
            'fields': ('marital_status', 'birth_date', 'nationality', 'phone_number', 'monthly_income')
        }),
    )
    
    list_filter = ('status', 'approved',)


class UserFormConfigurationAdmin(admin.ModelAdmin):
    form = UserFormConfigurationForm


admin.site.register(UserFormConfiguration, UserFormConfigurationAdmin)
admin.site.register(CustomerAnalysis, CustomerAnalysisAdmin)