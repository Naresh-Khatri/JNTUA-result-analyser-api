# Generated by Django 3.2 on 2021-05-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results_api', '0006_subject_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semestergpa',
            name='percentile',
            field=models.FloatField(default=0),
        ),
    ]
