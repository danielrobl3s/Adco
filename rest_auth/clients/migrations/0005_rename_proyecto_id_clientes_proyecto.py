# Generated by Django 4.1.7 on 2023-04-25 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0004_clientes_proyecto_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clientes", old_name="proyecto_id", new_name="proyecto",
        ),
    ]
