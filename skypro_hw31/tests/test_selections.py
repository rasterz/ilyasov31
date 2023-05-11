import json

import pytest
from rest_framework import status

from django.urls import reverse


@pytest.mark.django_db
def test_create_selection(api_client, user, ad):
    data = {
        'name': 'adnametestgfdgd',
        'owner': user.id,
        'items': [ad.id],
    }
    url = reverse('selection_create')
    expected_response = api_client.post(
        url,
        data=json.dumps(data),
        content_type='application/json',
    )
    expected_data = expected_response.json()
    assert expected_response.status_code == status.HTTP_201_CREATED
    assert expected_data['name'] == data['name']
    assert expected_data['owner'] == data['owner']
