# Generated by Django 4.0.1 on 2022-02-06 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=512)),
                ('tag', models.CharField(choices=[('BG', 'BUG'), ('AM', 'AMELIORATION'), ('TA', 'TACHE')], default='BG', max_length=2)),
                ('priority', models.CharField(choices=[('FA', 'FAIBLE'), ('MO', 'MOYENNE'), ('EL', 'ÉLEVÉE')], default='FA', max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('AF', 'A FAIRE'), ('EC', 'EN COURS'), ('TM', 'TERMINÉ')], default='AF', max_length=2)),
                ('assignee_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_project', to='projects.project')),
            ],
        ),
    ]
