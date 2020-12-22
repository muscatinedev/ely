# Generated by Django 3.1.3 on 2020-11-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('costcenters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodAndService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=60, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('costCenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costcenters.costcenter')),
            ],
        ),
    ]