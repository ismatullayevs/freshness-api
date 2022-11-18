# Generated by Django 4.1.2 on 2022-11-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_item_discount"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="tags",
            field=models.ManyToManyField(blank=True, to="products.tag"),
        ),
    ]
