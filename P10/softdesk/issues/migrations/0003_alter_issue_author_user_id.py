# Generated by Django 4.0.1 on 2022-02-18 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0002_alter_issue_author_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='author_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
