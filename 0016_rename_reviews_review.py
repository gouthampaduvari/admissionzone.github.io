# Generated by Django 4.2.1 on 2023-06-06 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0015_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
