# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-04 12:55
from __future__ import unicode_literals

import Account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile_img',
            field=models.ImageField(default='profile/default.png', upload_to='profile', verbose_name='프로필 사진'),
        ),
    ]
