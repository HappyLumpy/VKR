# Generated by Django 4.0.1 on 2022-01-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoadAccidentPoint',
            fields=[
                ('_id', models.JSONField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('geometry', models.JSONField(null=True)),
                ('properties', models.JSONField(null=True)),
                ('inwater', models.BooleanField()),
                ('coordinatesisaccurate', models.BooleanField()),
                ('inregion', models.JSONField(null=True)),
                ('onroad', models.BooleanField()),
                ('distancedif', models.FloatField(default=None, null=True)),
                ('yandexgeocoder', models.JSONField(default=None, null=True)),
                ('adminlevel', models.JSONField(null=True)),
                ('dtptime', models.JSONField(null=True)),
                ('valid', models.BooleanField()),
                ('validpercent', models.IntegerField()),
            ],
        ),
    ]
