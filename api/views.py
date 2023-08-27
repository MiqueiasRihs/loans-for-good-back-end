from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import CustomerAnalysisSerializer

from api.integrations.loan_processor import LoanProcessor

from loans_for_good.models import CustomerAnalysis
from loans_for_good.utils import EnumMaritalStatusOptions

class CustomerAnalysisView(APIView):
    def post(self, request):
        data = CustomerAnalysisSerializer(data=request.data)

        if data.is_valid():
            data.validated_data.setdefault("marital_status", EnumMaritalStatusOptions.SINGLE)

            try:
                customer = CustomerAnalysis.objects.create(**data.validated_data)

                loan_processor = LoanProcessor()
                loan_processor.loan_request(customer)

                return Response({'message': 'Dados recebidos com sucesso!'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Erro ao criar objeto CustomerAnalysis'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
