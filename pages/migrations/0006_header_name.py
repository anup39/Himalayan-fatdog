# Generated by Django 3.1.4 on 2020-12-16 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201216_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, help_text='this name for the definition only', max_length=200, verbose_name='header name'),
            preserve_default=False,
        ),
    ]