# Generated by Django 3.1.2 on 2021-01-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20210110_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='about',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
