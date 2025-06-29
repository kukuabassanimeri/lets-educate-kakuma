# Generated by Django 5.1.6 on 2025-06-18 23:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship_post', '0015_alter_ourimpact_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourimpact',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='ourimpact',
            name='date',
        ),
        migrations.AddField(
            model_name='ourimpact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
