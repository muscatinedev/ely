# Generated by Django 3.1.3 on 2020-12-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20201215_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooktime_1_temp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooktime_2_temp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooktime_3_temp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
