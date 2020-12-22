# Generated by Django 3.1.3 on 2020-12-15 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_cookingprogram_cookingprogramphase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookingprogram',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cookProgram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.cookingprogram'),
        ),
    ]
