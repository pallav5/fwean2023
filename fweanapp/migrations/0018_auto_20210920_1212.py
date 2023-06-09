# Generated by Django 2.1 on 2021-09-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0017_auto_20210709_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='imagealbum',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='membershipcontents',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='newsandmedia',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='programmes',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='successstories',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
    ]
