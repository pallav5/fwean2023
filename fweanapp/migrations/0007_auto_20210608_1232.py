# Generated by Django 3.1 on 2021-06-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0006_auto_20210608_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmes',
            name='image',
            field=models.ImageField(upload_to='Programmes'),
        ),
    ]
