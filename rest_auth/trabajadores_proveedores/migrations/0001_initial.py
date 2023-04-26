# Generated by Django 4.1.7 on 2023-04-25 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TrabajadoresProveedores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("telefono", models.CharField(max_length=15)),
                ("correo", models.EmailField(max_length=254)),
                ("direccion", models.TextField()),
                ("especialidad", models.CharField(max_length=100)),
                ("concepto", models.TextField()),
                ("archivos", models.FileField(upload_to="archivos/")),
                ("contratos", models.FileField(upload_to="contratos/")),
                ("monto_contrato", models.FloatField()),
                ("abonos", models.FloatField()),
                ("saldo", models.FloatField()),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
