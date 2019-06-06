# Generated by Django 2.2.1 on 2019-06-06 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('credit_limit', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerStanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(max_length=3)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentTypeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=3)),
                ('lat', models.CharField(max_length=11)),
                ('lng', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Tug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=20)),
                ('last_lng', models.CharField(max_length=11)),
                ('last_lat', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=60)),
                ('current_sequence', models.IntegerField()),
                ('finished', models.BooleanField()),
                ('barge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Barge')),
                ('tug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Tug')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('arrival_expected', models.IntegerField()),
                ('arrival_actual', models.IntegerField()),
                ('departure_expected', models.IntegerField()),
                ('departure_actual', models.IntegerField()),
                ('service_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ServiceCenter')),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('billto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments_billed_to', to='main_app.Customer')),
                ('consignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments_consigned_to', to='main_app.Customer')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments_delivering', to='main_app.ServiceCenter')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Equipment')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments_originating', to='main_app.ServiceCenter')),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments_shipped_by', to='main_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_by', models.CharField(max_length=60)),
                ('note', models.CharField(max_length=255)),
                ('date_time', models.IntegerField(max_length=20)),
                ('card_last_four', models.IntegerField(max_length=4)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.PaymentMethod')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ServiceCenter')),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.EquipmentTypeDetails'),
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=10)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=50)),
                ('address_city', models.CharField(max_length=50)),
                ('address_state', models.CharField(max_length=50)),
                ('address_zip', models.IntegerField(max_length=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='standing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.CustomerStanding'),
        ),
    ]
