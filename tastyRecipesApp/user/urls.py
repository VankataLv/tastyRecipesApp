from django.urls import path

from tastyRecipesApp.user.views import profile_create_page, profile_details_page, profile_edit_page, profile_delete_page

urlpatterns = [
    path('create/', profile_create_page, name='profile-create-page'),
    path('details/', profile_details_page, name='profile-details-page'),
    path('edit/', profile_edit_page, name='profile-edit-page'),
    path('delete/', profile_delete_page, name='profile-delete-page'),
    ]





