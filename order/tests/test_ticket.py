from django.test import TestCase
from django.urls import reverse
from ..models import Ticket, OrderItem, Equipment
from recipe.models import MenuItem
from django.contrib.auth import get_user_model

User = get_user_model()


class TicketViewTests(TestCase):
    def setUp(self):
        # Set up any objects that are needed for the tests
        self.user = User.objects.create_user(username="user", password="testpass")
        self.client.login(username="user", password="testpass")

        self.equipment = Equipment.objects.create(name="Main POS")
        self.menu_item1 = MenuItem.objects.create(name="Burger", price=10.00)
        self.menu_item2 = MenuItem.objects.create(name="Fries", price=5.00)

        self.url = reverse(
            "order:ticket_create"
        )  # Make sure 'create_ticket' is the name of the URL in your urls.py

    def test_create_ticket_and_order_items(self):
        # Test posting to the create ticket view
        response = self.client.post(
            self.url,
            {
                "equipment": self.equipment.id,
                "status": "placed",
                "orderitem_set-TOTAL_FORMS": "2",
                "orderitem_set-INITIAL_FORMS": "0",
                "orderitem_set-0-item": self.menu_item1.id,
                "orderitem_set-0-quantity": "2",
                "orderitem_set-1-item": self.menu_item2.id,
                "orderitem_set-1-quantity": "1",
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(Ticket.objects.exists())
        self.assertTrue(OrderItem.objects.exists())
        self.assertEqual(OrderItem.objects.count(), 2)

        self.assertEqual(response.json()["status"], "success")
        self.assertTrue("ticket_id" in response.json())
