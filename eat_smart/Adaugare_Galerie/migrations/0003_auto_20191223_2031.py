# Generated by Django 3.0.1 on 2019-12-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adaugare_Galerie', '0002_auto_20191220_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='mancare',
            name='username_autor',
            field=models.CharField(default='NON Autor', max_length=50),
        ),
        migrations.AlterField(
            model_name='mancare',
            name='upload',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
