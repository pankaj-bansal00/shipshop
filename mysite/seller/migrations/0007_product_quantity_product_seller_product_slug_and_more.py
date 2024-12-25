# Generated by Django 5.1.4 on 2024-12-24 18:39

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0006_seller_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="seller.seller",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default="temporary", editable=False, populate_from="name", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="categories/"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="name", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]