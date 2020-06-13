# Generated by Django 2.2.5 on 2020-06-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='collection_drive_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.collection_drive'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='donation_drive_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.donation_drive'),
        ),
    ]
