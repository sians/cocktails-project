from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200, default="Recipe Name")
    image = models.ImageField(upload_to='images/recipes/', blank=True)
    summary = models.CharField(max_length=200, blank=True)
    pass

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200, default="Ingredient Name")
    image = models.ImageField(upload_to='images/ingredients/', blank=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name

class Dose(models.Model):
    description = models.CharField(max_length=200, blank=True)
    recipe = models.ForeignKey(Recipe, related_name='doses', on_delete=models.CASCADE,)
    ingredient = models.ForeignKey(Ingredient, related_name='doses', on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Dose"
        verbose_name_plural = "Doses"
