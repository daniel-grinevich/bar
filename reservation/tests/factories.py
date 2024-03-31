import factory
import random
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from ..models import Event, Reservation
from location.tests.factories import TableFactory, LocationFactory
from users.tests.factories import CustomUserFactory

fake = Faker()


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    name = fake.name()
    cover = factory.LazyFunction(lambda: round(random.uniform(10.00, 100.00), 2))


def generate_random_time_this_week():
    now = timezone.now()
    start_of_week = now - timedelta(days=now.weekday())
    random_minute = random.randint(0, 59)
    random_hour = random.randint(8, 22)  # Assuming business hours from 8 AM to 10 PM
    random_day = random.randint(0, 6)
    generated_start_time = start_of_week.replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + timedelta(days=random_day, hours=random_hour, minutes=random_minute)
    return generated_start_time


def generate_time_without_conflict(table, location):
    while True:
        candidate = generate_random_time_this_week()
        reservation_durations = [
            timedelta(minutes=45),
            timedelta(hours=1),
            timedelta(hours=1, minutes=15),
            timedelta(hours=1, minutes=30),
            timedelta(hours=1, minutes=45),
            timedelta(hours=2),
        ]
        reservation_block = random.choice(reservation_durations)

        candidate_end_time = candidate + reservation_block
        if candidate.date() == candidate_end_time.date():
            opening_time = candidate.replace(hour=8, minute=0, second=0, microsecond=0)
            closing_time = candidate.replace(hour=22, minute=0, second=0, microsecond=0)

            if (
                opening_time <= candidate < closing_time
                and candidate_end_time <= closing_time
            ):
                conflicting_reservations = Reservation.objects.filter(
                    table=table,
                    location=location,
                    start_time__lt=candidate_end_time,
                    end_time__gt=candidate,
                ).exists()

                if not conflicting_reservations:
                    return candidate, reservation_block


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    event = factory.SubFactory(EventFactory)
    custom_user = factory.SubFactory(CustomUserFactory)
    status = factory.LazyFunction(
        lambda: random.choice(["pending", "confirmed", "cancelled"])
    )
    source = factory.LazyFunction(
        lambda: random.choice(["online", "phone", "in_person"])
    )
    location = factory.SubFactory(LocationFactory)
    special_requests = ""
    deposit_paid = False
    updated_at = timezone.now()
    table = factory.SubFactory(TableFactory)  # Ensure this is your TableFactory
    number_of_people = factory.LazyAttribute(
        lambda obj: random.randint(1, obj.table.chairs)
    )
    start_time = timezone.now()
    end_time = timezone.now()
    date = None

    @factory.post_generation
    def set_times(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        # Generate start_time and reservation_block together to avoid inconsistency
        generated_start_time, reservation_block = generate_time_without_conflict(
            self.table, self.location
        )
        self.start_time = generated_start_time
        self.end_time = generated_start_time + reservation_block
        self.date = self.start_time.date()

        # Since we're bypassing the factory's built-in handling by directly assigning
        # these values, we need to save the instance if it's already been created.
        self.save()
