# Generated by Django 5.0.4 on 2024-04-30 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20200610_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=255),
        ),
    ]
