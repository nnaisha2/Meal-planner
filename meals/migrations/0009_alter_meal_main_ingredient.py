# Generated by Django 5.1.4 on 2024-12-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0008_alter_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='main_ingredient',
            field=models.CharField(max_length=1000),
        ),
    ]