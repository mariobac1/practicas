# Generated by Django 3.0.4 on 2020-03-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingenierias', '0005_auto_20200311_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingenieriagsm',
            name='Ganancia',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
