from django.core.management.base import BaseCommand
import random
from recipe.tests.factories import (
    CategoryFactory,
    MenuItemFactory,
    MenuFactory,
    OptionFactory,
    ClassificationFactory,
)


class Command(BaseCommand):
    help = "Populates the database with dummy data"

    def handle(self, *args, **options):
        # Create categories
        cocktail_categories = ["Shaken", "Stirred", "Tiki", "Beer", "Seltzer"]
        hex_colors = ["#EAFAF3", "#EAC2CA", "#F1EAFA", "#CCEAFD", "#FFFACD"]
        categories = [
            CategoryFactory(color=color, name=name)
            for color, name in zip(hex_colors, cocktail_categories)
        ]
        class_names = ["Diary", "Garnish", "Extra", "Syrups", "Ice"]
        classification = [
            ClassificationFactory(color=color, name=name)
            for color, name in zip(hex_colors, class_names)
        ]

        # Create menu items
        cocktail_names = [
            "Margarita",
            "Old Fashioned",
            "Cosmopolitan",
            "Negroni",
            "Mojito",
            "Whiskey Sour",
            "Martini",
            "Pina Colada",
            "Bloody Mary",
            "Manhattan",
            "Daiquiri",
            "Mai Tai",
            "Tequila Sunrise",
            "Gin Fizz",
            "Caipirinha",
            "Long Island Iced Tea",
            "Sazerac",
            "French 75",
            "Mint Julep",
            "Moscow Mule",
            "Tom Collins",
            "Espresso Martini",
            "Aperol Spritz",
            "Aviation",
            "Dark 'n' Stormy",
            "Rum Punch",
            "Gimlet",
            "Sidecar",
            "Harvey Wallbanger",
            "Amaretto Sour",
        ]
        menuitems = [
            MenuItemFactory(name=name, categories=[random.choice(categories)])
            for name in cocktail_names
        ]

        customization_options = [
            "Extra Shot of Espresso",
            "Shot of Vanilla Syrup",
            "Shot of Caramel Syrup",
            "Splash of Almond Milk",
            "Splash of Oat Milk",
            "Splash of Coconut Milk",
            "Add Whipped Cream",
            "Sugar-Free Sweetener",
            "Extra Ice",
            "No Ice",
            "Salted Rim",
            "Sugared Rim",
            "Add Mint Leaves",
            "Add Lemon Slice",
            "Add Lime Slice",
            "Double Shot",
            "Half-Caff",
            "Decaf Coffee",
            "Extra Foam",
            "Chilled",
            "Heated",
            "With Ginger",
            "With Honey",
            "Spicy",
            "With Tonic",
            "With Soda",
            "With Ginger Ale",
            "Low Calorie",
            "Organic Ingredients",
            "Gluten-Free",
        ]

        options = [
            OptionFactory(
                name=option,
                categories=[random.choice(categories)],
                classification=random.choice(classification),
            )
            for option in customization_options
        ]

        # Create a menu and randomly assign a list of menu items
        # Ensuring at least one MenuItem is selected
        menus = [
            MenuFactory(
                items=random.sample(menuitems, k=random.randint(1, len(menuitems) // 2))
            )
            for _ in range(5)
        ]

        self.stdout.write(self.style.SUCCESS(f"{len(menuitems)} Menu Items created"))


# locations = [LocationFactory() for _ in range(5)]
# tables = [
#     TableFactory(location=location) for location in locations for _ in range(2)
# ]
# reservations = [
#     ReservationFactory(table=table, location=table.location)
#     for table in tables
#     for _ in range(2)
# ]

# self.stdout.write(
#     self.style.SUCCESS(f"{len(reservations)} Reservations created")
# )
