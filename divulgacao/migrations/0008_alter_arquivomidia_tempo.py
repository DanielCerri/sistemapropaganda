# Generated by Django 5.0.4 on 2024-04-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulgacao', '0007_arquivomidia_tempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivomidia',
            name='tempo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
