import json

import pytest
from rest_framework import status

from django.urls import reverse


@pytest.mark.django_db
def test_create_ad(api_client, user):
    data = {
        'name': 'adnametestgfdgd',
        'author': user.id,
        'price': 100,
    }
    url = reverse('ad_create')
    expected_response = api_client.post(
        url,
        data=json.dumps(data),
        content_type='application/json',
    )
    expected_data = expected_response.json()
    assert expected_data['name'] == data['name']
    assert expected_data['price'] == data['price']
    assert expected_data['author'] == data['author']


@pytest.mark.django_db
def test_list_ad(api_client):
    url = reverse('ad_list')
    expected_response = api_client.get(url)
    assert expected_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_ad_by_id(api_client, ad):
    url = reverse('ad_detail', kwargs={'pk': ad.id})
    expected_response = api_client.get(url)
    assert expected_response.status_code == status.HTTP_200_OK
    assert expected_response.json()['id'] == ad.id
