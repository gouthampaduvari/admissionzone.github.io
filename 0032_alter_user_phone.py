# Generated by Django 4.2.1 on 2023-07-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0031_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
