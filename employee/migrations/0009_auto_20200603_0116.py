# Generated by Django 2.2.6 on 2020-06-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20200602_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='employee'),
        ),
    ]
