# Generated by Django 5.0.4 on 2024-04-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='long_url',
            field=models.URLField(primary_key=True, serialize=False, verbose_name='Url original'),
        ),
    ]
