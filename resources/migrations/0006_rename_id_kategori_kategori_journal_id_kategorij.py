# Generated by Django 3.2.8 on 2021-12-13 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_alter_journal_kategorij'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategori_journal',
            old_name='id_kategori',
            new_name='id_kategorij',
        ),
    ]