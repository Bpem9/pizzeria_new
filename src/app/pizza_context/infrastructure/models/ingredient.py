from django.db import models


class Ingredient(models.Model):
    name = models.TextField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pizza_ingredient'
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
