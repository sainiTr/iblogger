# Generated by Django 4.1 on 2022-09-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Html', '0005_digitalpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalpage',
            name='page',
            field=models.TextField(),
        ),
    ]
