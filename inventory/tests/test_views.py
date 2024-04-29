from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
import pytest
from ..forms import PurchaseForm
from ..models import Purchase, PurchaseItem


def test_purchase_form_valid(db, new_purchase_form, client):
    form = PurchaseForm(new_purchase_form)
    print(form.errors)
    assert form.is_valid


@pytest.mark.parametrize(
    "url_name, redirect",
    [
        ("inventory:purchases_create", "inventory:purchases_item_edit"),
    ],
)
def test_purchase_form_post_redirects(
    db, url_name, redirect, new_purchase_form, client
):
    url = reverse(url_name)
    response = client.post(url, data=new_purchase_form)
    pk = Purchase.objects.get(name="Purchase A").pk
    assertRedirects(response, reverse(redirect, kwargs={"pk": pk}))


def test_purchase_item_form_set_valid(db, new_purchase_item_form_set, client):
    print(new_purchase_item_form_set.errors)
    assert new_purchase_item_form_set.is_valid


def test_deliver_purchase(db, new_purchase_with_item, client):
    purchase_item = new_purchase_with_item["purchase_item"]
    purchase = new_purchase_with_item["purchase"]

    item_quantity = purchase_item.quantity
    initial_product_quantity = purchase_item.product.quantity
    response = client.post(
        reverse(
            "inventory:purchases_deliver",
            kwargs={"pk": purchase.pk},
        )
    )
    purchase.refresh_from_db()
    purchase_item.refresh_from_db()

    errors = []
    if not purchase.delivered:
        errors.append("Purchase not delivered.")
    if (
        not new_purchase_with_item["purchase_item"].product.quantity
        == item_quantity + initial_product_quantity
    ):
        errors.append("Product not updated correctly.")
    if not response.status_code == 302:
        errors.append("Response returned wrong status code.")
    assert not errors, "errors occured:\n{}".format("\n".join(errors))
