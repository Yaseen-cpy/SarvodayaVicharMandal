# Generated by Django 4.2.3 on 2024-01-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_stories_thumbnail_height_stories_thumbnail_width_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
