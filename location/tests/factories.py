# factories.py
import factory
import random
from factory.django import DjangoModelFactory
from ..models import Location, Table
from faker import Faker

fake = Faker()


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.LazyFunction(lambda: fake.company())
    """
    Dynamically set `default` based on existing entries
    The lambda function will return False if True exists
    Return True if no True exits. Higher order function lol.
    """
    default = factory.LazyAttribute(
        lambda o: not Location.objects.filter(default=True).exists()
    )


class TableFactory(DjangoModelFactory):
    class Meta:
        model = Table

    name = factory.LazyFunction(lambda: fake.name())
    available = factory.LazyFunction(lambda: random.randint(1, 100) % 2 == 0)
    style = factory.LazyFunction(lambda: random.choice(["bar", "indoor", "outdoor"]))
    location = factory.SubFactory(LocationFactory)
    chairs = factory.LazyFunction(lambda: random.randint(1, 6))
