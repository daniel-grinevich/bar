import factory
from faker import Faker
from users.tests.factories import CustomUserFactory
from ..models import Order, OrderItem
from recipe.tests.factories import MenuItemFactory
import random
from django.utils import timezone


fake = Faker()


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    custom_user = factory.SubFactory(CustomUserFactory)
    customer = fake.name()
    total = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))
    tip = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))
    date_time = timezone.now()
    reservation = None
    status = factory.LazyFunction(
        lambda: random.choice(["placed", "preparing", "completed", "canceled"])
    )


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    item = factory.SubFactory(MenuItemFactory)
    quantity = factory.LazyFunction(lambda: random.randint(1, 9))
