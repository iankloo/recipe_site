from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
	#ingredients = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 10}))
	#directions = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 10}))

	class Meta:
		model = Recipe
		fields = ('title', 'author', 'short_desc', 'ingredients', 'directions', 'categories')

