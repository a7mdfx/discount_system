# Generated by Django 5.1.5 on 2025-02-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rule_name", models.CharField(max_length=100)),
                (
                    "min_order_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "percentage",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                (
                    "max_discount_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
            ],
        ),
    ]
