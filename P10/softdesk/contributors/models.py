from django.db import models


class Contributors(models.Model):

    class PermissionTextChoices(models.TextChoices):
        USER = ('R', "READ")
        owner = ('RW', "READ&WRITE")

    
    class RoleTextChoices(models.TextChoices):
        DEV = ('D', "DÉVELOPPEUR")
        PROJECT_OWNER = ('PW', "PROJECT OWNER")
    

        
    user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name="user_contrib")
    project_id = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name="project_contrib")
    permission = models.CharField(
        choices=PermissionTextChoices.choices,
        default=PermissionTextChoices.USER,
        max_length=2
    )

    role = models.CharField(
        choices=RoleTextChoices.choices,
        default=RoleTextChoices.DEV,
        max_length=2
    )