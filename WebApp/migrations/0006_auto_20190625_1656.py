# Generated by Django 2.2.2 on 2019-06-25 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_auto_20190623_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='Register_DateTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 25, 16, 56, 34, 981036)),
        ),
    ]