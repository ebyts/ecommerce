# Generated by Django 4.2.4 on 2023-08-31 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descroption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descroption',
            new_name='description',
        ),
    ]
