# Generated by Django 5.1.4 on 2024-12-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_alter_meal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
