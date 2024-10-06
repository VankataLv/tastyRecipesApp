from django.shortcuts import render

from tastyRecipesApp.user.models import Profile


def index(request):

    profile_obj = Profile.objects.first()

    context = {'user': profile_obj}

    return render(request, 'common/home-page.html', context)
