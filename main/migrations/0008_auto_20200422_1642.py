# Generated by Django 2.2.10 on 2020-04-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200422_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, to='main.ImageModel'),
        ),
    ]
