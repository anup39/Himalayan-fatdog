# Generated by Django 3.1.4 on 2021-01-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210109_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAlerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('on_off', models.BooleanField(default=True, verbose_name='Trun on/off email alerts')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emailing alert settings',
            },
        ),
    ]
