# Generated by Django 3.2.9 on 2022-12-05 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_employee_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='uid',
        ),
    ]
