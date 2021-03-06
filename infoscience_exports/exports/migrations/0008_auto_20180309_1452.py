# Generated by Django 2.0.2 on 2018-03-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exports', '0007_merge_20180309_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='groupsby_doc',
            field=models.CharField(choices=[('NONE', ''), ('DOC', 'document type'), ('DOC_TITLE', 'document type as title')], default='NONE', max_length=255),
        ),
        migrations.AlterField(
            model_name='export',
            name='groupsby_type',
            field=models.CharField(choices=[('NONE', ''), ('YEAR_TITLE', 'year as title'), ('DOC', 'document type'), ('DOC_TITLE', 'document type as title')], default='NONE', max_length=255),
        ),
        migrations.AlterField(
            model_name='export',
            name='groupsby_year',
            field=models.CharField(choices=[('NONE', ''), ('YEAR_TITLE', 'year as title')], default='NONE', max_length=255),
        ),
    ]
