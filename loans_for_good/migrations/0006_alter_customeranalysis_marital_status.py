# Generated by Django 4.2.4 on 2023-08-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_for_good', '0005_userformconfiguration_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeranalysis',
            name='marital_status',
            field=models.SmallIntegerField(choices=[(1, ' --- '), (2, 'Solteiro'), (3, 'Casado'), (4, 'Divorciado'), (5, 'Viúvo')], default=1, verbose_name='Estado civil'),
        ),
    ]
