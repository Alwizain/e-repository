# Generated by Django 3.2 on 2022-02-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_pembelian_nama_belakang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembelian',
            name='nama_belakang',
            field=models.CharField(max_length=30),
        ),
    ]
