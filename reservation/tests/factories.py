import factory
from faker import Faker
from ..models import Event
import random


fake = Faker()


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    name = factory.LazyFunction(fake.name)
    cover = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))


# class Event(models.Model):
# name = models.CharField(max_length=100, null=False)
# cover = models.DecimalField()
