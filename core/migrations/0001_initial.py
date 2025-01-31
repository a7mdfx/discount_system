# Generated by Django 5.1.5 on 2025-01-16 05:30

import django.db.models.deletion
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
        migrations.CreateModel(
            name="UserProfile",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("orders_count", models.IntegerField(default=0)),
                (
                    "total_spent",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("loyalty_status", models.CharField(default="Basic", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("subtotal", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "discount_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("final_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("status", models.CharField(default="pending", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="core.userprofile",
                    ),
                ),
            ],
        ),
    ]
