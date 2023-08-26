from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerAnalysisSerializer

from .models import CustomerAnalysis

class CustomerAnalysisView(APIView):
    def post(self, request):
        serializer = CustomerAnalysisSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            document = serializer.validated_data['document']
            email = serializer.validated_data['email']

            # Imprime os dados na tela
            print(f'Nome: {name}')
            print(f'Documento: {document}')

            CustomerAnalysis.objects.create(
                name=name,
                document=document,
                email=email
            )

            return Response({'message': 'Dados recebidos com sucesso!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
