# Generated by Django 2.2.24 on 2021-12-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20211206_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
