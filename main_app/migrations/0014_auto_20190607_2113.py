# Generated by Django 2.2.1 on 2019-06-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20190607_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='credit_limit',
            field=models.IntegerField(blank=True, default=2000),
        ),
    ]
