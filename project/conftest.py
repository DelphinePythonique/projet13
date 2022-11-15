import pytest

from lettings.models import Address, Letting

@pytest.fixture(scope='function')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        Address.objects.create(
            number=7,
            street="pius street",
            city="Paris",
            state="NY",
            zip_code="75014",
            country_iso_code="FRA",
        )

