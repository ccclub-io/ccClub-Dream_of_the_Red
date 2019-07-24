# Generated by Django 2.2.1 on 2019-07-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=15)),
                ('number', models.CharField(max_length=30)),
                ('credit', models.PositiveIntegerField()),
                ('time', models.CharField(max_length=30)),
            ],
        ),
    ]
