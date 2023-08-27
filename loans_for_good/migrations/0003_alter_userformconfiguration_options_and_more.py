# Generated by Django 4.2.4 on 2023-08-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_for_good', '0002_remove_userformconfiguration_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userformconfiguration',
            options={'verbose_name': 'Formulario de análise', 'verbose_name_plural': 'Formularios de análise'},
        ),
        migrations.AlterField(
            model_name='userformconfiguration',
            name='field_settings',
            field=models.JSONField(default=dict, unique=True),
        ),
    ]