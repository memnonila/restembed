# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedEmbeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
                ('provider_url', models.URLField()),
                ('provider_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('descripttion', models.TextField()),
                ('html', models.TextField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('thumbnail_url', models.URLField()),
                ('thumbnail_width', models.IntegerField()),
                ('thumbnail_height', models.IntegerField()),
                ('author_url', models.URLField()),
                ('author_name', models.CharField(max_length=100)),
                ('version', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
    ]
