# Generated by Django 5.1.1 on 2024-10-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_cuisine_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine_type',
            field=models.CharField(choices=[('French', 'French'), ('Chinese', 'Chinese'), ('Italian', 'Italian'), ('Balkan', 'Balkan'), ('Other', 'Other')], max_length=7),
        ),
    ]
