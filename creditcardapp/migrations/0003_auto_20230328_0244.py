# Generated by Django 3.2.18 on 2023-03-28 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcardapp', '0002_auto_20230328_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 28, 2, 44, 17, 976142))),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('massage', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='creditcardapply',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 28, 2, 44, 17, 974140)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 28, 2, 44, 17, 973140)),
        ),
    ]
