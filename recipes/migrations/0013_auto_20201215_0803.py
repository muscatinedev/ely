# Generated by Django 3.1.3 on 2020-12-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_remove_recipeitem_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooktime_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooktime_3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
