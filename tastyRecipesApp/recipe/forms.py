from django import forms

from tastyRecipesApp.recipe.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)
        widgets = {
            'ingredients': forms.Textarea(
                attrs={'placeholder': 'ingredient1, ingredient2, ...'}
            ),
            'instructions': forms.Textarea(
                attrs={'placeholder': 'Enter detailed instructions here...',}
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Optional image URL here...',}
            ),
        }


class RecipeEditForm(forms.ModelForm):
        class Meta:
            model = Recipe
            exclude = ('author',)


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
