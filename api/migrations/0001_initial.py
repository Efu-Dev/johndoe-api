# Generated by Django 4.2.3 on 2023-07-14 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=9)),
                ('genero', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, unique=True)),
                ('marca', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('color', models.CharField(max_length=45)),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('tipo', models.CharField(max_length=1)),
                ('estado', models.CharField(default='P', max_length=1)),
                ('resultados', models.TextField(null=True)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
    ]