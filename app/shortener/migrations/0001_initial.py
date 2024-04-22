# Generated by Django 5.0.4 on 2024-04-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(help_text='Máximo de 15 caracteres', max_length=15, unique=True, verbose_name='Código curto')),
                ('long_url', models.URLField(verbose_name='Url original')),
                ('expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de validade')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
                'db_table': 'urls',
            },
        ),
    ]