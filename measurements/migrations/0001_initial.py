# Generated by Django 3.1.3 on 2020-11-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('nn', 'Numeric'), ('vl', 'Volume'), ('wt', 'Weight')], max_length=20)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
