import pytest
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


@pytest.fixture(scope='function')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        address = Address.objects.create(
            number=7,
            street="pius street",
            city="Paris",
            state="NY",
            zip_code="75014",
            country_iso_code="FRA",
        )
        Letting.objects.create(

            title="my pius address",
            address=address
        )

        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Profile.objects.create(
            user=user,
            favorite_city="Paris"
        )
