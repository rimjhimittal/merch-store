# Generated by Django 4.1.4 on 2023-01-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_size_chart_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url1',
            field=models.URLField(blank=True, default=None, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url2',
            field=models.URLField(blank=True, default=None, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_chart_url',
            field=models.URLField(blank=True, default=None, max_length=5000, null=True),
        ),
    ]
