# Generated by Django 2.1 on 2021-12-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0023_emailrecipients_membership_membershiporganization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmembers',
            name='president_image',
            field=models.ImageField(upload_to='BoardMembers'),
        ),
    ]
