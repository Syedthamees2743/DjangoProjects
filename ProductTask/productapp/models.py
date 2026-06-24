from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"),
        ("Food", "Food"),
        ("Books", "Books"),
        ("Clothes", "Clothes"),
    ]

    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )
    description = models.TextField()

    def __str__(self):
        return self.name
