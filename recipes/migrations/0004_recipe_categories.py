# Generated by Django 3.0.3 on 2020-03-30 17:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200223_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Appetizer', 'Appetizer'), ('Breakfast', 'Breakfast'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Drink', 'Drink'), ('Salad', 'Salad'), ('Bread', 'Bread'), ('Soup', 'Soup'), ('Grilling', 'Grilling')], max_length=66, null=True),
        ),
    ]
