# Generated by Django 3.1.4 on 2020-12-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_socialheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('full_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Enquiry',
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]