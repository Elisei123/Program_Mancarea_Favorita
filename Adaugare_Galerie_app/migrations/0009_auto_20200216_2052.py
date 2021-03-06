# Generated by Django 3.0.3 on 2020-02-16 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Adaugare_Galerie_app', '0008_mancare_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mancare',
            name='favorites',
        ),
        migrations.AlterField(
            model_name='favorit',
            name='id_mancare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adaugare_Galerie_app.Mancare'),
        ),
        migrations.AlterField(
            model_name='favorit',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
