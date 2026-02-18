from django.core.management.base import BaseCommand
from reservation.models import Table


class Command(BaseCommand):
    help = "Seed initial restaurant tables"

    def handle(self, *args, **kwargs):
        tables = [
            {"number": 1, "seat": 2, "location": "Window"},
            {"number": 2, "seat": 4, "location": "Center"},
            {"number": 3, "seat": 6, "location": "Patio"},
            {"number": 4, "seat": 8, "location": "VIP Room"},
            {"number": 5, "seat": 4, "location": "Window"},
        ]

        for table_data in tables:
            table, created = Table.objects.get_or_create(
                number=table_data["number"],
                defaults={
                    "seat": table_data["seat"],
                    "location": table_data["location"],
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created Table {table.number}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Table {table.number} already exists"
                    )
                )
