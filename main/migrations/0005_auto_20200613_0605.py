# Generated by Django 2.2.5 on 2020-06-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200612_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='filepath',
            field=models.FileField(default='', upload_to='files/'),
        ),
    ]
