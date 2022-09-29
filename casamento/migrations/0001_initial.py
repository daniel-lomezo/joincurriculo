# Generated by Django 4.1 on 2022-09-29 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ListaCasamento",
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
                (
                    "nome_item",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Nome do Item",
                    ),
                ),
                (
                    "medida_item",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Medida do Item",
                    ),
                ),
                (
                    "preferencia_cor",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Preferência de cor",
                    ),
                ),
            ],
        ),
    ]