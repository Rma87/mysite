# Generated by Django 3.2.25 on 2024-06-28 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_titele_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cotent',
            new_name='content',
        ),
    ]