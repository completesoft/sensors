# Generated by Django 2.1.5 on 2019-01-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datastring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('devid', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID устройства')),
                ('temp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Температура')),
            ],
        ),
    ]
