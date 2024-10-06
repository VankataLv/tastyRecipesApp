from django.urls import path, include

from tastyRecipesApp.recipe.views import catalogue_page, recipe_create_page, recipe_details_page, recipe_edit_page, \
    recipe_delete_page

urlpatterns = [
    path('catalogue/', catalogue_page, name='catalogue-page'),
    path('create/', recipe_create_page, name='recipe-create-page'),
    path('<int:recipe_id>', include([
        path('details/', recipe_details_page, name='recipe-details-page'),
        path('edit/', recipe_edit_page, name='recipe-edit-page'),
        path('delete/', recipe_delete_page, name='recipe-delete-page'),
    ]))
]
