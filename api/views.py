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
            name = data.validated_data["name"] if data["name"].value else None
            document = data.validated_data["document"] if data["document"].value else None
            email = data.validated_data["email"] if data["email"].value else None
            marital_status = data.validated_data["marital_status"] if data["marital_status"].value else EnumMaritalStatusOptions.SINGLE
            birth_date = data.validated_data["birth_date"] if data["birth_date"].value else None
            nationality = data.validated_data["nationality"] if data["nationality"].value else None
            phone_number = data.validated_data["phone_number"] if data["phone_number"].value else None
            monthly_income = data.validated_data["monthly_income"] if data["monthly_income"].value else None
            
            customer = CustomerAnalysis.objects.create(
                name=name,
                document=document,
                email=email,
                marital_status=marital_status,
                birth_date=birth_date,
                nationality=nationality,
                phone_number=phone_number,
                monthly_income=monthly_income,
            )
            
            loan_processor = LoanProcessor()
            loan_processor.loan_request(customer)

            return Response({'message': 'Dados recebidos com sucesso!'}, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
