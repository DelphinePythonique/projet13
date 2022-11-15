import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_view(client):
    url = reverse("lettings:lettings_index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content
