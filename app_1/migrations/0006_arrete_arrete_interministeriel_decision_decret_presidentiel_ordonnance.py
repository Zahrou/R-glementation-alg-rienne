# Generated by Django 2.1.2 on 2018-11-07 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_remove_decret_executif_loi'),
    ]

    operations = [
        migrations.CreateModel(
            name='arrete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('objet', models.CharField(max_length=2000)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.jarida')),
            ],
        ),
        migrations.CreateModel(
            name='arrete_interministeriel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('objet', models.CharField(max_length=2000)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.jarida')),
            ],
        ),
        migrations.CreateModel(
            name='decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('objet', models.CharField(max_length=2000)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.jarida')),
            ],
        ),
        migrations.CreateModel(
            name='decret_presidentiel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('objet', models.CharField(max_length=2000)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.jarida')),
            ],
        ),
        migrations.CreateModel(
            name='ordonnance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('objet', models.CharField(max_length=2000)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.jarida')),
            ],
        ),
    ]