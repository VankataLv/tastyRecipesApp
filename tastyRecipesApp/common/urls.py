from django.urls import path

from tastyRecipesApp.common import views

urlpatterns = [
    path('', views.index, name='home-page'),
]