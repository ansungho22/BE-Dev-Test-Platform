# Generated by Django 3.2.5 on 2021-08-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Instagram",
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
                ("Title", models.CharField(max_length=20)),
                ("Context", models.TextField()),
                ("UploadImage", models.URLField()),
                ("UploadTime", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["UploadTime"],
            },
        ),
    ]
