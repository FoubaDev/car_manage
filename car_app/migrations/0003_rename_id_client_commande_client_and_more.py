# Generated by Django 4.1.7 on 2023-03-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_alter_personne_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='id_client',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='commande',
            old_name='id_voiture',
            new_name='voiture',
        ),
    ]
