# Generated by Django 4.2.13 on 2024-06-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0010_free_emoji_move_emoji"),
    ]

    operations = [
        migrations.AddField(
            model_name="free",
            name="ftcontent",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="free",
            name="emoji",
            field=models.TextField(),
        ),
    ]