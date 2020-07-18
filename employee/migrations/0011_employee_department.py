# Generated by Django 2.2.6 on 2020-06-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20200610_1248'),
        ('employee', '0010_auto_20200603_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='department.Department'),
        ),
    ]
