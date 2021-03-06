# Generated by Django 3.1.4 on 2020-12-29 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutuspage',
            name='header_title',
        ),
        migrations.RemoveField(
            model_name='aboutuspage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutuspage',
            name='title',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='first_title',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=200, verbose_name='first title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='second_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='second title'),
        ),
    ]
