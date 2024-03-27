# factories.py
import factory
from factory.django import DjangoModelFactory
from ..models import Location
from faker import Faker

fake = Faker()


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.LazyFunction(lambda: fake.user_name())
    default = False
