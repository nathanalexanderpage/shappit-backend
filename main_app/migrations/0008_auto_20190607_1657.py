# Generated by Django 2.2.1 on 2019-06-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20190606_2105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EquipmentTypeDetails',
            new_name='EquipmentType',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='id',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]