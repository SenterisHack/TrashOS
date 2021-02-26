# Generated by Django 3.1.7 on 2021-02-26 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(verbose_name='Координата X')),
                ('y', models.FloatField(verbose_name='Координата Y')),
                ('display_address', models.CharField(max_length=100, verbose_name='Отображаемый адрес')),
            ],
        ),
        migrations.CreateModel(
            name='TrashSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=64, verbose_name='Отображаемое название')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('trash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trashos_server.trash')),
            ],
        ),
        migrations.CreateModel(
            name='TrashSensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Время')),
                ('data', models.FloatField(verbose_name='Заполненость')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trashos_server.trashsensor')),
            ],
        ),
    ]