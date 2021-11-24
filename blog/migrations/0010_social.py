# Generated by Django 3.1.4 on 2020-12-19 11:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201216_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='title')),
                ('slug', models.SlugField(blank=True, help_text='will be generated automatically if left blank', max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d', verbose_name='image')),
                ('show', models.BooleanField(default=True, verbose_name='show')),
                ('brief', models.CharField(blank=True, max_length=120, null=True, verbose_name='small brief')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'Social work',
                'verbose_name_plural': 'Social work',
                'ordering': ('-updated_at',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
