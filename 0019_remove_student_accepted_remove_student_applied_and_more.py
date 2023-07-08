# Generated by Django 4.2 on 2023-06-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0018_remove_student_status_student_accepted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='student',
            name='applied',
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='notapplied', max_length=50),
        ),
    ]
