# Generated by Django 2.0.3 on 2018-03-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exports', '0011_auto_20180321_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='show_summary',
            field=models.BooleanField(default=False),
        ),
    ]
