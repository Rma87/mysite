# Generated by Django 3.2.25 on 2024-06-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_published_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titele',
            new_name='title',
        ),
    ]
