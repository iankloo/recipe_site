# Generated by Django 3.0.3 on 2020-04-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20200330_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
    ]
