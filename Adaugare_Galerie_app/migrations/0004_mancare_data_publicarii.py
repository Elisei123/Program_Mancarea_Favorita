# Generated by Django 3.0.1 on 2019-12-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adaugare_Galerie_app', '0003_auto_20191223_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='mancare',
            name='data_publicarii',
            field=models.CharField(default='NON Data', max_length=50),
        ),
    ]
