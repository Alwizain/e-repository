# Generated by Django 3.2 on 2022-02-22 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembelian',
            name='metode_pembayaran',
        ),
        migrations.RemoveField(
            model_name='pembelian',
            name='nomor_akun',
        ),
        migrations.AddField(
            model_name='pembelian',
            name='token',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='pembelian',
            name='tgl_transaksi',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
