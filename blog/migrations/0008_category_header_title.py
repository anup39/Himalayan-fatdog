# Generated by Django 3.1.4 on 2020-12-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='header_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='header title'),
        ),
    ]
