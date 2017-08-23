# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-21 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_auto_20160214_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gym',
            options={'ordering': ['name'], 'permissions': (('gym_trainer', 'Trainer: can see the users for a gym'), ('manage_gym', 'Admin: can manage users for a gym'), ('manage_gyms', 'Admin: can administrate the different gyms'))},
        ),
        migrations.AlterField(
            model_name='contract',
            name='options',
            field=models.ManyToManyField(blank=True, to='gym.ContractOption', verbose_name='Options'),
        ),
        migrations.AlterField(
            model_name='gymadminconfig',
            name='overview_inactive',
            field=models.BooleanField(default=True, help_text='Receive email overviews of inactive members', verbose_name='Overview of inactive members'),
        ),
        migrations.AlterField(
            model_name='gymconfig',
            name='weeks_inactive',
            field=models.PositiveIntegerField(default=4, help_text='Number of weeks since the last time a user logged his presence to be considered inactive', verbose_name='Reminder of inactive members'),
        ),
    ]
