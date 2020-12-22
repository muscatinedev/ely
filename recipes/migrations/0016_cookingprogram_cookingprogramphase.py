# Generated by Django 3.1.3 on 2020-12-15 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20201215_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookingProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='CookingProgramPhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chamber', models.CharField(choices=[('op', 'Open'), ('cl', 'Closed')], max_length=20)),
                ('cookTime', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.cookingprogram')),
            ],
        ),
    ]
