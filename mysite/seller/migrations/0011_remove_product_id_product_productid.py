# Generated by Django 5.1.4 on 2024-12-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0010_alter_category_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.AddField(
            model_name="product",
            name="Productid",
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
