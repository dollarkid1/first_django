# Generated by Django 3.2.7 on 2021-09-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Native',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('cohort', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='natic.cohort')),
            ],
        ),
    ]
