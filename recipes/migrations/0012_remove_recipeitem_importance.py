# Generated by Django 3.1.3 on 2020-12-14 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_recipeitem_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeitem',
            name='importance',
        ),
    ]
