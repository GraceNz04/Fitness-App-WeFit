# Generated by Django 4.2.13 on 2024-05-28 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=20)),
                ('description', models.TextField(blank=True)),
                ('demonstration', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=40)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness_app.exercise')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness_app.user')),
            ],
        ),
    ]
