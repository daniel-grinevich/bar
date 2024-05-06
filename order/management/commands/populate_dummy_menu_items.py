from django.core.management.base import BaseCommand
from recipe.tests.factories import MenuItemFactory


class Command(BaseCommand):
    help = "Populates the database with dummy data"

    def handle(self, *args, **options):
        menu_item = [MenuItemFactory() for _ in range(5)]
        self.stdout.write(self.style.SUCCESS(f"{len(menu_item)} Menu Item(s) created"))
