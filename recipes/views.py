from django.shortcuts import render, get_object_or_404

from .models import Ingredient, Recipe, Dose

# Create your views here.
def index(request):
    recipes = Recipe.objects
    return render(request, 'recipes/index.html', {'recipes': recipes})

def show(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/show.html', {'recipe': recipe})
