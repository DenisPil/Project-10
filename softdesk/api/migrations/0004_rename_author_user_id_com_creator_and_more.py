# Generated by Django 4.0.1 on 2022-01-24 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220123_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='com',
            old_name='author_user_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='author_user_id',
            new_name='creator',
        ),
    ]
