import pytest

from django.urls import reverse
from project13.project.conftest import django_db_setup as my_django_db_setup # noqa


@pytest.mark.django_db
def test_lettings_index_view(client):
    url = reverse("lettings:lettings_index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content


@pytest.mark.django_db
def test_lettings_letting_view(client, my_django_db_setup): # noqa
    url = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(url)
    assert response.status_code == 200
    assert b"<title>my pius address</title>" in response.content
