# Generated by Django 3.2.5 on 2021-08-20 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_tvshow_libera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='libera',
        ),
    ]
