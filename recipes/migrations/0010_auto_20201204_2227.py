# Generated by Django 3.1.3 on 2020-12-04 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_auto_20201204_0207'),
        ('categories', '0001_initial'),
        ('measurements', '0001_initial'),
        ('recipes', '0009_auto_20201204_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='uom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.uom'),
        ),
    ]
