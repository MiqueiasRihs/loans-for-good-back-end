from django.contrib import admin
from django.urls import path, include

admin.autodiscover()
admin.site.site_header = u'Loans For Good - Back office '

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/', include('api.urls')),
]
