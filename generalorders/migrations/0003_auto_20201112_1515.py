# Generated by Django 3.1.3 on 2020-11-12 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalorders', '0002_auto_20201112_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='uon',
            new_name='uom',
        ),
    ]
