from django.contrib import admin
# from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Recipe, Dose, Ingredient

class DoseInline(admin.TabularInline):
    model = Dose

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        DoseInline,
    ]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
