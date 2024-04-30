from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
import pytest
from ..forms import BarInventoryProductForm
from ..models import Purchase, PurchaseItem

# Test Froms are Valid


@pytest.mark.parametrize(
    "form",
    [
        ("new_purchase_form"),
        ("new_product_category_form"),
        ("new_brand_form"),
        ("new_bar_inventory_product_form"),
        ("new_bar_inventory_item_form"),
        ("new_purchase_item_form_set"),
    ],
)
def test_purchase_form_valid(db, form, request):
    form = request.getfixturevalue(form)
    assert not form.errors


@pytest.mark.parametrize(
    "url_name, redirect",
    [
        (
            "inventory:purchases_create",
            "inventory:purchases_item_edit",
        ),
    ],
)
def test_purchase_form_post_redirects(
    db, url_name, redirect, new_purchase_form_data, client
):
    url = reverse(url_name)
    response = client.post(url, data=new_purchase_form_data)
    pk = Purchase.objects.get(name="Purchase A").pk
    assertRedirects(response, reverse(redirect, kwargs={"pk": pk}))


@pytest.mark.parametrize(
    "url_name, redirect, form_data",
    [
        (
            "inventory:brands_create",
            "inventory:brands",
            "new_brand_form_data",
        ),
        (
            "inventory:categories_create",
            "inventory:categories",
            "new_product_category_form_data",
        ),
        (
            "inventory:inventory_item_create",
            "inventory:inventory_items",
            "new_bar_inventory_item_form_data",
        ),
        (
            "inventory:inventory_product_create",
            "inventory:inventory_products",
            "new_bar_inventory_product_form_data",
        ),
    ],
)
def test_form_redirects_list_view(db, url_name, redirect, client, form_data, request):
    url = reverse(url_name)
    form_data = request.getfixturevalue(form_data)
    response = client.post(url, data=form_data)
    assertRedirects(response, reverse(redirect))


# Test Delivery
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
        errors.append("Product quantity not updated correctly upon delivery.")
    if not response.status_code == 302:
        errors.append("Response returned wrong status code.")

    purchase.delivered = False
    purchase.save()
    purchase_item.refresh_from_db()

    if purchase.delivered:
        errors.append("Purchase not undelivered.")
    if (
        not new_purchase_with_item["purchase_item"].product.quantity
        == initial_product_quantity
    ):
        errors.append("Product not updated correctly upon undelivery.")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
