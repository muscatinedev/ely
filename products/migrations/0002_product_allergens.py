# Generated by Django 3.1.3 on 2020-11-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='allergens',
            field=models.ManyToManyField(to='allergens.Allergen'),
        ),
    ]
