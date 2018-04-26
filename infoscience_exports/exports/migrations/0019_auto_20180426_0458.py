# Generated by Django 2.0.3 on 2018-04-26 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exports', '0018_auto_20180426_0458'),
    ]

    operations = [
        migrations.DeleteModel('LegacyExport'),
        migrations.CreateModel(
            name='LegacyExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('export', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='exports.Export')),
                ('legacy_id', models.IntegerField(blank=True, null=True)),
                ('content_delta', models.IntegerField(blank=True, null=True)),
                ('legacy_url', models.TextField()),
                ('language', models.TextField()),
                ('referenced_url', models.TextField()),
                ('origin', models.TextField(
                    choices=[('OTHER', ''), ('JAHIA', 'Jahia'),
                             ('PEOPLE', 'People')])),
                ('origin_sciper', models.TextField()),
                ('origin_id', models.TextField()),
                ('raw_csv_entry', models.TextField()),
            ],
        ),
    ]