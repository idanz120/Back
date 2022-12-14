# Generated by Django 4.0.6 on 2022-08-07 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='departure_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flights',
            name='destination_country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.countries'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='landing_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flights',
            name='origin_country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.countries'),
        ),
    ]
