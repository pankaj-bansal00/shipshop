# Generated by Django 5.1.4 on 2024-12-27 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={},
        ),
        migrations.AlterModelManagers(
            name="customer",
            managers=[],
        ),
        migrations.RenameField(
            model_name="customer",
            old_name="mobile",
            new_name="mobile_number",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user_permissions",
        ),
    ]