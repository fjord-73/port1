# Generated by Django 3.1.2 on 2021-04-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port1', '0002_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]