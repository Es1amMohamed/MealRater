# Generated by Django 4.2.5 on 2023-09-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mealrater", "0002_alter_rating_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
