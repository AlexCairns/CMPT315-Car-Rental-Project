# Generated by Django 4.1.3 on 2022-11-30 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_rename_licenceplate_car_licenseplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='Employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.employee'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='TotalCost',
            field=models.FloatField(blank=True, null=True),
        ),
    ]