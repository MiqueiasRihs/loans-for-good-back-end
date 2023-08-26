from django.urls import path

from .views import CustomerAnalysisView

urlpatterns = [
    path('analise-de-cliente/', CustomerAnalysisView.as_view(), name='CustomerAnalysisView'),
]
