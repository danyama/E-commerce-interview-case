# Generated by Django 2.2.24 on 2021-12-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_auto_20211207_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='venda',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
    ]
