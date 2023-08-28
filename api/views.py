from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import CustomerAnalysisSerializer

from api.integrations.loan_processor import LoanProcessor

from loans_for_good.models import CustomerAnalysis, UserFormConfiguration
from loans_for_good.utils import FIELD_OPTIONS_DICT

class CustomerAnalysisView(APIView):
    def post(self, request):
        data = CustomerAnalysisSerializer(data=request.data)

        if data.is_valid():
            try:
                customer = CustomerAnalysis.objects.create(**data.validated_data)

                loan_processor = LoanProcessor()
                loan_processor.loan_request(customer)

                return Response({'message': 'Dados recebidos com sucesso! iremos análisar seus dados e logo lhe damos a resposta.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Erro ao criar objeto CustomerAnalysis'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        fields_data = UserFormConfiguration.objects.filter().order_by('-id').first()
        
        if fields_data:
            fields_data = [FIELD_OPTIONS_DICT[field] for field in fields_data.field_settings]
        
            return Response({'fields': fields_data}, status=status.HTTP_200_OK)
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        