# Generated by Django 2.2.1 on 2019-07-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20190724_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='class_code',
            field=models.CharField(default=None, max_length=30),
        ),
    ]