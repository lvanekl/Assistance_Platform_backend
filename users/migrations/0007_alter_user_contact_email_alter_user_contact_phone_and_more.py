# Generated by Django 4.1.2 on 2023-01-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_phone',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_tg',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_vk',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
    ]
