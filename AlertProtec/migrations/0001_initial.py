# Generated by Django 3.2 on 2023-06-15 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_machinery', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('num_serial', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=2010)),
                ('capacity', models.IntegerField(default=0)),
                ('type_fuel', models.CharField(max_length=50)),
                ('hour', models.IntegerField(default=0)),
                ('date_maintenance', models.DateField(verbose_name='date maintenance')),
                ('status', models.CharField(max_length=100)),
                ('type_engine', models.CharField(max_length=100)),
                ('img', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_birth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('certifications', models.CharField(max_length=200)),
                ('rol', models.IntegerField(default=0)),
                ('machinery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AlertProtec.machinery')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('rol', models.IntegerField(default=0)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('avatar', models.CharField(blank=True, max_length=250)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertProtec.person')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertProtec.person')),
            ],
        ),
    ]
