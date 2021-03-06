# Generated by Django 3.1.3 on 2020-11-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('goodsandservices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Brand Name', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product Name', max_length=60)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('goodOrService', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goodsandservices.goodandservice')),
            ],
        ),
    ]
