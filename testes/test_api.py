import pytest, json

from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

from loans_for_good.models import UserFormConfiguration
from loans_for_good.utils import FIELD_OPTIONS_DICT

def create_test_data():
    return {
        "name": "usuario_teste",
        "document": "76508775073"
    }

@pytest.mark.django_db
def test_create_customer_analysis():
    client = APIClient()
    url = reverse('CustomerAnalysisView')

    data = create_test_data()

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_customer_analysis_error():
    client = APIClient()
    url = reverse('CustomerAnalysisView')

    # Data with no document info
    data = {
        "name": "usuario_teste"
    }

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
@pytest.mark.django_db
def test_get_user_form_configuration():
    client = APIClient()
    url = reverse('CustomerAnalysisView')

    user_form_fields = UserFormConfiguration.objects.create(
        name="form_test",
        field_settings=["email", "marital_status", "birth_date", "nationality", "phone_number", "monthly_income"]
    )

    response = client.get(url)
    response_format = response.json()['fields']
    fields_data = [FIELD_OPTIONS_DICT[field] for field in user_form_fields.field_settings]

    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response_format) == json.dumps(fields_data)

@pytest.mark.django_db
def test_get_user_form_configuration_no_data():
    client = APIClient()
    url = reverse('CustomerAnalysisView')

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

