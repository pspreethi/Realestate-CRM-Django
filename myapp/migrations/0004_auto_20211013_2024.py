# Generated by Django 3.2 on 2021-10-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_client_remarks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.AddField(
            model_name='client',
            name='doj',
            field=models.DateField(null=True),
        ),
    ]
