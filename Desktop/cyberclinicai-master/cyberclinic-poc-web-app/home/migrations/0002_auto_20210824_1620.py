# Generated by Django 2.1.15 on 2021-08-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
