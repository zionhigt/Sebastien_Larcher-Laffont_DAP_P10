from django.db import models


class Issue(models.Model):

    class PriorityTextChoices(models.TextChoices):
        FAIBLE = ('FA', 'FAIBLE')
        MOYENNE = ('MO', 'MOYENNE')
        ELEVEE = ('EL', 'ÉLEVÉE')

    class TagTextChoices(models.TextChoices):
        BUG = ('BG', 'BUG')
        AMELIORATION = ('AM', 'AMELIORATION')
        TACHE = ('TA', 'TACHE')

    class StatusTextChoices(models.TextChoices):
        A_FAIRE = ('AF', 'A FAIRE')
        EN_COURS = ('EC', 'EN COURS')
        TERMINE = ('TM', 'TERMINÉ')

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=512)
    tag = models.CharField(
        choices=TagTextChoices.choices,
        default=TagTextChoices.BUG,
        max_length=2
        )
    priority = models.CharField(
        choices=PriorityTextChoices.choices,
        default=PriorityTextChoices.FAIBLE,
        max_length=2
        )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    project_id = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='issue_project')
    status = models.CharField(
        choices=StatusTextChoices.choices,
        default=StatusTextChoices.A_FAIRE,
        max_length=2
        )
    author_user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='issue_author')
    assignee_user_id = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name="issue_assignee"
        )
