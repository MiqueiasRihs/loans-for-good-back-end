from django.contrib import admin
from django.urls import path

from loans_for_good.views import CustomerAnalysisView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documento/', CustomerAnalysisView.as_view(), name='documento'),
]
