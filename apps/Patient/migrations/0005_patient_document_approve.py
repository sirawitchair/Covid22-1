# Generated by Django 3.2.12 on 2022-03-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_auto_20220305_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='document_approve',
            field=models.BooleanField(default=False, verbose_name='มีใบวิทยุ'),
        ),
    ]