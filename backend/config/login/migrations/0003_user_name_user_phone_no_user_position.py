# Generated by Django 4.1.4 on 2022-12-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('MB', 'Member'), ('CR', 'Core'), ('JS', 'Joint Secretary'), ('GS', 'General Secretary')], default='MB', max_length=2),
        ),
    ]
