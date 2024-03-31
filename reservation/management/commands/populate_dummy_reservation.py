from django.core.management.base import BaseCommand
from location.tests.factories import LocationFactory, TableFactory
from reservation.tests.factories import ReservationFactory


class Command(BaseCommand):
    help = "Populates the database with dummy data"

    def handle(self, *args, **options):
        locations = [LocationFactory() for _ in range(5)]
        tables = [
            TableFactory(location=location) for location in locations for _ in range(2)
        ]
        reservations = [
            ReservationFactory(table=table, location=table.location)
            for table in tables
            for _ in range(2)
        ]

        self.stdout.write(
            self.style.SUCCESS(f"{len(reservations)} Reservations created")
        )
