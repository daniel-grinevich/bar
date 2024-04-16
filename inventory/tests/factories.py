import factory
import random
from faker import Faker
from django.utils import timezone
from ..models import (
    Brands,
    ProductCategory,
    Purchase,
    BarInventoryProduct,
    PurchaseItem,
    BarInventoryItem,
)
from location.tests.factories import TableFactory, LocationFactory
from users.tests.factories import CustomUserFactory

fake = Faker()


class BrandsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brands

    name = factory.Sequence(lambda n: "Brand%d" % n)


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductCategory

    name = factory.Sequence(lambda n: "Category%d" % n)


class PurchaseItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PurchaseItem

    purchase = factory.SubFactory("inventory.tests.factories.PurchaseFactory")
    date_purchased = timezone.now().date
    quantity = factory.LazyAttribute(lambda obj: random.randint(1, 99))
    product = factory.SubFactory("inventory.tests.factories.BarInventoryProductFactory")


class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    name = factory.Sequence(lambda n: "Purchase%d" % n)

    class Params:
        with_purchase_items = factory.Trait(
            item_1=factory.RelatedFactory(PurchaseItemFactory)
        )


class BarInventoryProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BarInventoryProduct

    name = factory.Sequence(lambda n: "Product%d" % n)
    category = factory.SubFactory(ProductCategoryFactory)
    size = factory.LazyAttribute(lambda obj: random.randint(1, 750))
    refridgerated = False
    brand = factory.SubFactory(BrandsFactory)
    par_level = factory.LazyAttribute(lambda obj: random.randint(1, 100))
    quantity = factory.LazyAttribute(lambda obj: random.randint(1, 100))
    location = factory.SubFactory(LocationFactory)


class BarInventoryItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BarInventoryItem

    name = factory.Sequence(lambda n: "InventoryItem%d" % n)
    date_expired = timezone.now().date
    location = factory.SubFactory(LocationFactory)
    product = factory.SubFactory(BarInventoryProductFactory)
    level = factory.LazyAttribute(lambda obj: random.randint(1, 100))