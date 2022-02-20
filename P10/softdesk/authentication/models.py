from django.contrib.auth.models import AbstractUser
from projects.models import Project
from contributors.models import Contributors


class User(AbstractUser):

    def is_project_contributor(self, project_id):
        project = Project.objects.get(pk=project_id)
        if project:
            contributors = Contributors.objects.filter(project_id=project_id)
            if contributors:
                contributors.get(user_id=self.pk)
                return bool(contributors or project.author_user_id.id == self.pk)

        return False
