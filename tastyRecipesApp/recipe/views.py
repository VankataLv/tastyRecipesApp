from django.shortcuts import render, redirect

from tastyRecipesApp.recipe.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from tastyRecipesApp.recipe.models import Recipe
from tastyRecipesApp.user.models import Profile


def catalogue_page(request):
    # user = Profile.objects.first()
    recipies_listed = Recipe.objects.all().order_by('pk')
    context = {
        # 'user': user,
        'recipies': recipies_listed
    }

    return render(request, 'recipe/catalogue.html', context)


def recipe_create_page(request):
    form = RecipeCreateForm(request.POST or None)
    user = Profile.objects.first()

    if request.method == 'POST' and form.is_valid():
        form.instance.author = user
        form.save()
        return redirect('catalogue-page')

    context = {'form': form}

    return render(request, 'recipe/create-recipe.html', context)


def recipe_details_page(request, recipe_id: int):
    selected_recipe = Recipe.objects.get(pk=recipe_id)
    ingredient_lst = selected_recipe.ingredients.split(', ')
    context = {
        'recipe': selected_recipe,
        'ingredients': ingredient_lst
    }

    return render(request, 'recipe/details-recipe.html', context)


def recipe_edit_page(request, recipe_id: int):
    selected_recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=selected_recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue-page')

    form = RecipeEditForm(instance=selected_recipe)

    context = {
        'recipe': selected_recipe,
        'form': form
               }

    return render(request, 'recipe/edit-recipe.html', context)


def recipe_delete_page(request, recipe_id: int):
    selected_recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        selected_recipe.delete()
        return redirect('catalogue-page')

    form = RecipeDeleteForm(instance=selected_recipe)

    context = {
        'recipe': selected_recipe,
        'form': form
    }

    return render(request, 'recipe/delete-recipe.html', context)
