# Generated by Django 3.1.4 on 2020-12-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201220_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d', verbose_name='image2'),
        ),
    ]