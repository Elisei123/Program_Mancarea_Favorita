# Generated by Django 3.0.1 on 2019-12-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adaugare_Galerie_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mancare',
            name='titlul',
            field=models.CharField(max_length=20),
        ),
    ]
