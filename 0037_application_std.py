# Generated by Django 4.2 on 2023-07-05 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0036_review_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='std',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std', to='admissionapp.student'),
        ),
    ]