from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200, default="Recipe Name")
    image = models.ImageField(upload_to='images/recipes/')
    summary = models.CharField(max_length=200)
    pass

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200, default="Ingredient Name")
    image = models.ImageField(upload_to='images/ingredients/')

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name

class Dose(models.Model):
    description = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,)
