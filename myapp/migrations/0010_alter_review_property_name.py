# Generated by Django 3.2 on 2021-10-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20211020_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='property_name',
            field=models.CharField(default='nothing', max_length=120),
        ),
    ]
