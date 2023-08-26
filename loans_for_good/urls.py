from django.contrib import admin
from django.urls import path

from loans_for_good.views import CustomerAnalysisView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analise-de-cliente/', CustomerAnalysisView.as_view(), name='CustomerAnalysisView'),
]
