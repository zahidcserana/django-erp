# Generated by Django 2.2.6 on 2020-05-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='SE', max_length=100),
        ),
    ]
