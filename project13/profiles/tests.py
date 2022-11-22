import pytest

from django.urls import reverse
from project13.project.conftest import django_db_setup as my_django_db_setup  # noqa


@pytest.mark.django_db
def test_view(client):
    url = reverse("profiles:profiles_index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"<title>Profiles</title>" in response.content


@pytest.mark.django_db
def test_profiles_profile_view(client, my_django_db_setup):  # noqa
    url = reverse("profiles:profile", kwargs={"username": "john"})
    response = client.get(url)
    assert response.status_code == 200
    assert b"<title>john</title>" in response.content
