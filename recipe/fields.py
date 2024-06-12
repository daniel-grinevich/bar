from django.db import models
import re
from django.core.exceptions import ValidationError


def validate_hex_color(value):
    pattern = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")
    valid_hex = bool(pattern.match(value))
    if not valid_hex:
        raise ValidationError(f"{value} is not a valid hex color code.")


class HexColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 7
        super().__init__(*args, **kwargs)
        self.validators.append(validate_hex_color)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
