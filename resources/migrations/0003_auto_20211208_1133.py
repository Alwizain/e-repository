# Generated by Django 3.2.8 on 2021-12-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20211208_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='id_buku',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='journal',
            name='kd_jurnal',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='id_kategori',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pengarang',
            name='id_pengarang',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
