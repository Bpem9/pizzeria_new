from django.db import models


class Pizza(models.Model):
    name = models.TextField()
    cost = models.IntegerField()
    ingredients = models.ManyToManyField(
        'pizza.Ingredient',
        related_name='pizzas'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pizza_pizza'
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'
