# Generated by Django 3.1 on 2021-06-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0007_auto_20210608_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Programmes'),
        ),
    ]
