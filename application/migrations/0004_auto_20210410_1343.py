# Generated by Django 3.0.5 on 2021-04-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='fullname',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='cvc',
            field=models.IntegerField(default=None),
        ),
    ]
