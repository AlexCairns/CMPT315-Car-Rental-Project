# Generated by Django 4.1.1 on 2022-10-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_customer_unitnumber_alter_employee_unitnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='DateReturned',
            field=models.DateField(blank=True, null=True),
        ),
    ]