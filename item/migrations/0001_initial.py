# Generated by Django 5.0 on 2023-12-22 21:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=60)),
                ("description", models.TextField()),
                (
                    "price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(50)]
                    ),
                ),
            ],
        ),
    ]
