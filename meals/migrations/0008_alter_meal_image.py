# Generated by Django 5.1.4 on 2024-12-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0007_alter_meal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(upload_to='meals/'),
        ),
    ]
