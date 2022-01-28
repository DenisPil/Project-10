# Generated by Django 4.0.1 on 2022-01-28 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('tag', models.CharField(choices=[('BUG', 'Bug'), ('UPGRADE', 'Upgrade'), ('TASK', 'Task')], max_length=8)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGHT', 'Hight')], max_length=8)),
                ('status', models.CharField(max_length=64)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee_user_id_issue', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_user_id_issue', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_id_for_project', to='project.project')),
            ],
        ),
    ]
