# Generated by Django 4.2.6 on 2023-10-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appcurriculo", "0002_experiencia_formacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experiencia",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="formacao",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]