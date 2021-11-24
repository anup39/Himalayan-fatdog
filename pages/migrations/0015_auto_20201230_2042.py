# Generated by Django 3.1.4 on 2020-12-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20201229_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='city',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='company',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='description',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='package',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Requested Package'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Contact Number'),
        ),
    ]