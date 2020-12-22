# Generated by Django 3.1.3 on 2020-11-30 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
        ('categories', '0001_initial'),
        ('ingredients', '0002_auto_20201112_0817'),
        ('recipes', '0003_wishtocookrecipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredients.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='uom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurements.uom'),
        ),
    ]