from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

catChoices = (('Appetizer', 'Appetizer'),
              ('Breakfast', 'Breakfast'),
              ('Dinner', 'Dinner'),
              ('Dessert', 'Dessert'),
              ('Drink', 'Drink'),
              ('Salad', 'Salad'),
              ('Bread', 'Bread'),
              ('Soup', 'Soup'),
              ('Grilling', 'Grilling'))

class Recipe(models.Model):
	date_added = models.DateTimeField(default=timezone.now)
	author = models.CharField(max_length = 100)
	ingredients = models.CharField(max_length = 5000)
	directions = models.CharField(max_length = 5000)
	title = models.CharField(max_length = 100)
	short_desc = models.CharField(max_length = 500)
	categories = MultiSelectField(choices = catChoices, null = True, blank = True)
