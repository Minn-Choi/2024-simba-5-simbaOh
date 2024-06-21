# Generated by Django 5.0.4 on 2024-06-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certification",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Education",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="certifications",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="education",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="experience",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="projects",
        ),
        migrations.AddField(
            model_name="portfolio",
            name="certifications",
            field=models.ManyToManyField(to="users.certification"),
        ),
        migrations.AddField(
            model_name="portfolio",
            name="education",
            field=models.ManyToManyField(to="users.education"),
        ),
        migrations.AddField(
            model_name="portfolio",
            name="experience",
            field=models.ManyToManyField(to="users.experience"),
        ),
        migrations.AddField(
            model_name="portfolio",
            name="projects",
            field=models.ManyToManyField(to="users.project"),
        ),
    ]