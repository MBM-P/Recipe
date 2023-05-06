from django.shortcuts import render, get_object_or_404, redirect

from .scraper import get_recipes_info
from .models import Recipe
from django.core.paginator import Paginator

def recipe_list(request):
    # get_recipes_info()
    recipes = Recipe.objects.all()
    #set up pagination 
    p= Paginator(Recipe.objects.all(),2)
    page = request.GET.get('page')
    recipe = p.get_page(page)
    
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes,'recipe':recipe})
