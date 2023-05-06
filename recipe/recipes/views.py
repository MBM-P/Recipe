from django.shortcuts import render, get_object_or_404, redirect

from .scraper import get_recipes_info
from .models import Recipe


def recipe_list(request):
    get_recipes_info()
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
