# Generated by Django 2.1.15 on 2021-08-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('main_id', models.BigIntegerField(blank=True, null=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
