# Generated by Django 3.1.4 on 2020-12-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20201216_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogheader',
            name='image',
            field=models.ImageField(upload_to='pages/blog/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='homeheader',
            name='video',
            field=models.FileField(upload_to='header'),
        ),
    ]
