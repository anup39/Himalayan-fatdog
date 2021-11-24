# Generated by Django 3.1.4 on 2020-12-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_header_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='main title')),
                ('header_title', models.CharField(max_length=200, verbose_name='second title')),
                ('image', models.ImageField(upload_to='pages/headers/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'BlogHeader',
                'verbose_name_plural': 'BlogHeader',
            },
        ),
    ]