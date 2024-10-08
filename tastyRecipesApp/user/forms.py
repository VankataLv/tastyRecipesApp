from django import forms

from tastyRecipesApp.user.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('bio', )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
