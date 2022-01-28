# Generated by Django 4.0.1 on 2022-01-28 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue', '0005_alter_issue_creator_alter_issue_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_user_id_issue', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
