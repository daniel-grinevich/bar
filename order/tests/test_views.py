from django.test import TestCase
from .factories import OrderFactory
from django.urls import reverse


class OrderListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for _ in range(5):
            OrderFactory()

    def test_object_listview_url_exists(self):
        url = reverse("order:order_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_object_listview_uses_correct_template(self):
        response = self.client.get(reverse("order:order_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order/order_list.html")
