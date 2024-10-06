from django.shortcuts import render


def profile_create_page(request):

    context = {}

    return render(request, 'user/create-profile.html', context)


def profile_details_page(request):

    context = {}

    return render(request, 'user/details-profile.html', context)


def profile_edit_page(request):

    context = {}

    return render(request, 'user/edit-profile.html', context)


def profile_delete_page(request):

    context = {}

    return render(request, 'user/delete-profile.html', context)
