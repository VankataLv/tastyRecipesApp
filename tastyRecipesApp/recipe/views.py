from django.shortcuts import render


def catalogue_page(request):

    context = {}

    return render(request, 'recipe/catalogue.html', context)


def recipe_create_page(request):

    context = {}

    return render(request, 'recipe/create-recipe.html', context)


def recipe_details_page(request, recipe_id: int):

    context = {}

    return render(request, 'recipe/details-recipe.html', context)


def recipe_edit_page(request, recipe_id: int):

    context = {}

    return render(request, 'recipe/edit-recipe.html', context)


def recipe_delete_page(request, recipe_id: int):

    context = {}

    return render(request, 'recipe/delete-recipe.html', context)