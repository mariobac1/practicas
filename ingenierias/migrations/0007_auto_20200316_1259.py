# Generated by Django 3.0.4 on 2020-03-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingenierias', '0006_auto_20200316_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingenierialte',
            name='Ganancia',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='ingenieriaumts',
            name='Ganancia',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
