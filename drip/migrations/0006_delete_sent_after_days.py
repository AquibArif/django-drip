# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0005_drip_template_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='drip',
            name='delete_sent_after_days',
            field=models.IntegerField(help_text='Delete sent_drips after number of days.', null=True, blank=True),
        ),
    ]
