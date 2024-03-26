# Generated by Django 5.0.3 on 2024-03-25 14:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]