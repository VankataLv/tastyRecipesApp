from django.shortcuts import render, redirect

from tastyRecipesApp.recipe.models import Recipe
from tastyRecipesApp.user.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from tastyRecipesApp.user.models import Profile


def profile_create_page(request):
    form = CreateProfileForm(request.POST or None)

    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('catalogue-page')

    return render(request, 'user/create-profile.html', context)


def profile_details_page(request):
    user = Profile.objects.first()
    published_recipes = Recipe.objects.filter(author=user)

    context = {
        'user': user,
        'recipe_count': len(published_recipes),
    }

    return render(request, 'user/details-profile.html', context)


def profile_edit_page(request):
    user = Profile.objects.first()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile-details-page')

    form = EditProfileForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'user/edit-profile.html', context)


def profile_delete_page(request):
    user = Profile.objects.first()
    form = DeleteProfileForm(instance=user)

    if request.method == 'POST':
        user.delete()
        return redirect('home-page')

    context = {
        'user': user,
        'form': form,
               }

    return render(request, 'user/delete-profile.html', context)
