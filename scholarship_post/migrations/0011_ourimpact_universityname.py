# Generated by Django 5.1.6 on 2025-06-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship_post', '0010_alter_ourimpact_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourimpact',
            name='universityName',
            field=models.CharField(default='Not Mentioned', max_length=100),
        ),
    ]
