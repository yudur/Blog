# Generated by Django 2.2.3 on 2022-07-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0004_auto_20220630_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='nome_comentario',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
    ]
