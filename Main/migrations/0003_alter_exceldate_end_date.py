# Generated by Django 4.2.4 on 2023-08-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_exceldate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exceldate',
            name='end_date',
            field=models.CharField(max_length=200),
        ),
    ]
