# Generated by Django 5.0.3 on 2024-06-21 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_mentor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='follow',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='follow_count',
        ),
    ]
