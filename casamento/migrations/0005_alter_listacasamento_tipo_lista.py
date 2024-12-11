# Generated by Django 5.1.4 on 2024-12-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casamento', '0004_listacasamento_quem_escolheu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listacasamento',
            name='tipo_lista',
            field=models.CharField(blank=True, choices=[('Lista chá de panela', 'chá de panela'), ('lista de casamento', 'presente de casamento')], default='Lista chá de panela', max_length=300, null=True, verbose_name='Tipo da Lista'),
        ),
    ]
