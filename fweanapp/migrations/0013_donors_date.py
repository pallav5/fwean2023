# Generated by Django 2.1 on 2021-07-08 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0012_blogcomments_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
