from rest_framework import serializers

from .models import CustomerAnalysis

class CustomerAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAnalysis
        fields = '__all__'
