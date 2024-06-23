# Generated by Django 5.0.3 on 2024-06-22 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_mentor_mentor_ship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='mentor_ship',
        ),
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_ship', models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menti_ship', to='main.mentor')),
            ],
        ),
    ]