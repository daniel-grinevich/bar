from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=100, null=True)
    chairs = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='number of chairs at a table'
    )
    available = models.BooleanField(default=True)
    BAR = 'bar'
    INDOOR = 'indoor'
    OUTDOOR = 'outdoor'
    TABLE_TYPE_CHOICES = [
        (BAR, 'Bar Table'),
        (INDOOR, 'Indoor Table'),
        (OUTDOOR, 'Outdoor Table'),
    ]
    style = models.CharField(max_length=20, choices=TABLE_TYPE_CHOICES)
    locatoin = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='tables'
    )

    def __str__(self):
        return f"Chairs: {self.name} (Location: {self.location.name})"
