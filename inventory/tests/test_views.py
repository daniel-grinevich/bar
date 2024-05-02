from django.urls import reverse
from pytest_django.asserts import assertRedirects
import pytest
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
    ],
)
def test_purchase_form_valid(db, form, request):
    form = request.getfixturevalue(form)
    assert not form.errors


@pytest.mark.parametrize(
    "formset",
    [
        ("new_purchase_item_form_set"),
    ],
)
def test_purchase_formset_valid(db, formset, request):
    formset = request.getfixturevalue(formset)
    assert formset.is_valid


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


def test_purchase_item_form_post_redirects(
    db, new_purchase_item_form_set_data, client, purchase_factory
):
    purchase = purchase_factory.create()
    pk = purchase.pk
    # pk = new_purchase_item_form_set_data["purchaseitem_set-0-purchase"]
    url = reverse("inventory:purchases_item_edit", kwargs={"pk": pk})
    response = client.post(url, data=new_purchase_item_form_set_data)
    assertRedirects(response, reverse("inventory:purchases_detail", kwargs={"pk": pk}))


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
