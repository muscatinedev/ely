# Generated by Django 3.1.3 on 2020-12-15 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_auto_20201215_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cooktime',
        ),
    ]
