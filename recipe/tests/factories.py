import factory
from faker import Faker
from users.tests.factories import CustomUserFactory
from ..models import Menu, MenuItem
import random

fake = Faker()


class MenuItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuItem

    name = fake.name()
    description = fake.paragraph()
    price = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))


class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Menu

    name = fake.name()
    description = fake.paragraph()
    items = factory.RelatedFactory(MenuItemFactory)
