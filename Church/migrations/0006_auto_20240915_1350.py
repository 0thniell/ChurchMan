# Generated by Django 3.2.25 on 2024-09-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Church', '0005_auto_20240915_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='gross',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='net',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
