from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .scraper import get_recipes_info
from .models import Recipe
from django.core.paginator import Paginator

def recipe_list(request):

    #get_recipes_info()
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipes/')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')

    # get_recipes_info()
    recipes = Recipe.objects.all()
    #set up pagination 
    p= Paginator(Recipe.objects.all(),2)
    page = request.GET.get('page')
    recipe = p.get_page(page)
    
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes,'recipe':recipe})
