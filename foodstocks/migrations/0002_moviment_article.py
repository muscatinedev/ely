# Generated by Django 3.1.3 on 2020-11-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
        ('foodstocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.article'),
        ),
    ]
