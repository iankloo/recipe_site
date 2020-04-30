from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from.forms import RecipeForm
from django.utils import timezone


def recipe_list(request):
	recs = Recipe.objects.all()
	
	return render(request, 'recipes/recipe_list.html', {'recs': recs})


def recipe_detail(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)

	return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.date_added = timezone.now()
            rec.save()
            return redirect('recipe_detail', pk=rec.pk)
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipe_edit.html', {'form': form})