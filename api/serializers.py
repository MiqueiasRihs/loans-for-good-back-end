from rest_framework import serializers

from loans_for_good.models import CustomerAnalysis

class CustomerAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAnalysis
        fields = '__all__'
