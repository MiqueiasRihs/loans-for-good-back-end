from rest_framework import serializers

from loans_for_good.models import CustomerAnalysis
from loans_for_good.utils import document_validation

from datetime import datetime

class CustomerAnalysisSerializer(serializers.ModelSerializer):
    formatted_document = serializers.SerializerMethodField()

    class Meta:
        model = CustomerAnalysis
        fields = '__all__'
    
    def to_internal_value(self, data):
        # Birth date validation
        birth_date = data.get('birth_date')
        if birth_date:
            try:
                birth_date = datetime.strptime(birth_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                data['birth_date'] = birth_date
            except ValueError:
                raise serializers.ValidationError({'message': 'Data de nascimento inválida'})
            
        # Document validation
        document = data.get('document')
        if document:
            document = ''.join(filter(str.isdigit, document))
            if not document_validation(document):
                raise serializers.ValidationError({'message': 'CPF inválido'})
            
        # Phone number validation
        phone_number = data.get('phone_number')
        if phone_number:
            data['phone_number'] = ''.join(filter(str.isdigit, phone_number))

        return super().to_internal_value(data)
