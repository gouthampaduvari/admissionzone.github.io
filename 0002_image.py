# Generated by Django 4.2.1 on 2023-05-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
