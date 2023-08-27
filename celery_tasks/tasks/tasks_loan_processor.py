import json, requests

from django.utils import timezone

from celery import shared_task

from loans_for_good.models import CustomerAnalysis
from loans_for_good.utils import EnumAnalysisStatus

@shared_task(queue='default')
def task_loan_request(url, headers, customer_id):
    customer = CustomerAnalysis.objects.get(pk=customer_id)
    response = requests.post(url, headers=headers, data=json.dumps({
        "name": customer.name,
        "document": customer.document
    }))
    
    print(response, "\n", response.json())

    if response.ok:
        content = response.json()
        
        customer.analyzed_at = timezone.now()
        customer.approved = content["approved"]
        customer.status = EnumAnalysisStatus.APPROVED if content["approved"] else EnumAnalysisStatus.DENIED
        customer.save()

    return