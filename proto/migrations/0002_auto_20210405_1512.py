# Generated by Django 3.1.2 on 2021-04-05 06:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='point',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)]),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proto.rank')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
