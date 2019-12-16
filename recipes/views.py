from django.shortcuts import render

from .models import Ingredient, Recipe, Dose

# Create your views here.
def index(request):
    recipes = Recipe.objects
    return render(request, 'recipes/index.html', {'recipes': recipes})
