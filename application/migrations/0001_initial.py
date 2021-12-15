# Generated by Django 3.0.5 on 2021-04-08 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.FileField(null=True, upload_to='static/images/uploads/destination')),
            ],
        ),
        migrations.CreateModel(
            name='Itenerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='static/images/uploads')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('main_Info', models.TextField(null=True)),
                ('country_Name', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField(blank=True)),
                ('destination', models.ManyToManyField(default=None, to='application.Destination')),
                ('itinerary', models.ManyToManyField(default=None, to='application.Itenerary')),
                ('reviews', models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
