from django.db import models
from contributors.models import Contributors


class Project(models.Model):

    class TypeTextChoices(models.TextChoices):
        CREATION = ('CR', 'CREATION')
        AMELIORATION = ('AM', 'AMELIORATION')
        EVOLUTION = ('EV', 'EVOLUTION')

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=512)
    type = models.CharField(
        choices=TypeTextChoices.choices,
        default=TypeTextChoices.CREATION,
        max_length=2
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author_user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='project_author')

    def is_own_contributor(self, user_id):
        contributors = Contributors.objects.filter(project_id=self.pk, user_id=user_id)

        if contributors and len(contributors):
            return True

        if self.author_user_id.id == user_id:
            return True

        return False
