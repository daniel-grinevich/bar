from django.urls import reverse
import pytest


def test_delivery(db, client, new_purchase_with_item):
    test = DeliveryTest(new_purchase_with_item)
    errors = test.test_deliver_purchase(client)
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

    errors = test.test_undeliver_purchase()
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


# Classes with constructors aren't pulled in by pytest
class DeliveryTest:
    def __init__(self, new_purchase_with_item):
        self.purchase = new_purchase_with_item["purchase"]
        self.purchase_item = new_purchase_with_item["purchase_item"]
        self.product = self.purchase_item.product
        self.initial_product_quantity = self.product.quantity

    def test_deliver_purchase(self, client):
        print(self.product.quantity)
        response = self.deliver_purchase(self.purchase.pk, client)
        self.purchase.refresh_from_db()
        self.purchase_item.refresh_from_db()
        self.product.refresh_from_db()
        print(self.product.quantity)
        errors = self.check_delivery_errors(response)

        return errors

    def test_undeliver_purchase(self):
        self.purchase.status = "ordered"
        self.purchase.save()
        self.purchase_item.refresh_from_db()
        self.product.refresh_from_db()
        errors = self.check_undelivery_errors()

        return errors

    def deliver_purchase(self, pk, client):
        return client.post(
            reverse(
                "inventory:purchase_deliver",
                kwargs={"pk": pk},
            )
        )

    def check_delivery_errors(self, response):
        errors = []
        if self.purchase.status != "delivered":
            errors.append("Purchase not delivered.")
        if (
            not self.product.quantity
            == self.purchase_item.quantity + self.initial_product_quantity
        ):
            errors.append("Product quantity not updated correctly upon delivery.")
        if not response.status_code == 302:
            errors.append("Response returned wrong status code.")
        return errors

    def check_undelivery_errors(self):
        errors = []
        if self.purchase.status == "delivered":
            errors.append("Purchase not undelivered.")
        if not self.product.quantity == self.initial_product_quantity:
            errors.append("Product not updated correctly upon undelivery.")
        return errors
