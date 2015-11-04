# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(to='lists.List', default=None),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]
