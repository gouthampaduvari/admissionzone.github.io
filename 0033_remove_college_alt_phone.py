# Generated by Django 4.2.1 on 2023-07-02 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0032_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='alt_phone',
        ),
    ]