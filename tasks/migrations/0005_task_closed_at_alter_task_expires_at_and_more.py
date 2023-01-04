# Generated by Django 4.1.2 on 2023-01-03 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='closed_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 21, 20, 38, 680299)),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('A', 'accepting applications'), ('P', 'in progress'), ('C', 'closed')], max_length=1),
        ),
    ]