# Generated by Django 4.2.5 on 2023-10-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_cozinha_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='codigo_entrada',
            field=models.IntegerField(unique=True),
        ),
    ]
