import factory
from faker import Faker
from users.tests.factories import CustomUserFactory
from ..models import Menu, MenuItem, Category, Option, Classification
import random
import secrets

fake = Faker()


def random_hex_color():
    return f"#{secrets.token_hex(3).upper()}"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyFunction(fake.name)
    color = factory.LazyFunction(random_hex_color)


class MenuItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuItem

    name = factory.LazyFunction(fake.name)
    description = factory.LazyFunction(fake.paragraph)
    price = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.categories.set(extracted)
        else:
            categories = [CategoryFactory() for _ in range(3)]
            self.categories.set(categories)


class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Menu

    name = factory.LazyFunction(fake.name)
    description = factory.LazyFunction(fake.paragraph)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.items.set(extracted)
        else:
            menu_items = [MenuItemFactory() for _ in range(3)]
            self.items.set(menu_items)


class ClassificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Classification

    name = factory.LazyFunction(fake.name)
    color = factory.LazyFunction(random_hex_color)


class OptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Option

    name = factory.LazyFunction(fake.name)
    price = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))
    classification = factory.SubFactory(Classification)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.categories.set(extracted)
        else:
            categories = [CategoryFactory() for _ in range(3)]
            self.categories.set(categories)
