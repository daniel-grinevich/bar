from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, null=False)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.default:
            """
            Select all other default locations and set them to not be the default
            The default location will be the one that prepopulates
            the reservation dashboard.
            """
            Location.objects.filter(default=True).update(default=False)
        super(Location, self).save(*args, **kwargs)


class Table(models.Model):
    name = models.CharField(max_length=100, null=True)
    chairs = models.IntegerField(
        null=False, blank=False, verbose_name="number of chairs at a table"
    )
    available = models.BooleanField(default=True)
    BAR = "bar"
    INDOOR = "indoor"
    OUTDOOR = "outdoor"
    TABLE_TYPE_CHOICES = [
        (BAR, "Bar Table"),
        (INDOOR, "Indoor Table"),
        (OUTDOOR, "Outdoor Table"),
    ]
    style = models.CharField(max_length=20, choices=TABLE_TYPE_CHOICES)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="tables"
    )

    def __str__(self):
        return f"Chairs: {self.name} (Location: {self.location.name})"
