# Generated by Django 3.2.8 on 2021-10-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_diarista_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarista',
            name='cidade',
            field=models.CharField(max_length=30),
        ),
    ]
