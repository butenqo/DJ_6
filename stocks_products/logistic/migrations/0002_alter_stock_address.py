# Generated by Django 4.2 on 2023-07-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
