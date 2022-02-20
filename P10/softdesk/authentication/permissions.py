from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Project


class NotUpdatable(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == "update":
            return False
        return True


class IsProjectDetailAccess(BasePermission):
    def has_object_permission(self, request, view, obj):
        project_id = int(obj.pk)
        project = Project.objects.get(pk=project_id)

        if not project:
            return False

        if project.is_own_contributor(request.user.id):
            return True

        return False


class IsAuthorOrReadonly(BasePermission):
    project_id = 'project_id'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:

            project = obj
            for k in self.project_id.split('.'):
                project = getattr(project, k)

            if project:
                print(project)
                return project.is_own_contributor(request.user.id)
        if obj.author_user_id.id == request.user.id:
            return True
        return False


# Aply on contributors viewset
class IsProjectAuthorOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        project = obj.project_id
        if request.method in SAFE_METHODS:
            return project.is_own_contributor(request.user.id)
        if project.author_user_id.id == request.user.id:
            return True
        return False


class IsIssueAuthorOrReadonly(IsAuthorOrReadonly):
    project_id = "project_id"


class IsCommentAuthorOrReadonly(IsAuthorOrReadonly):
    project_id = 'issue_id.project_id'


class ProjectContributors(BasePermission):
    def has_permission(self, request, view):

        try:
            project_id = int(view.kwargs.get('project_id_pk'))
        except ValueError:
            print(view.kwargs.get('project_id_pk') + " n'est pas un identifiant valide")
            return False

        project = Project.objects.get(pk=project_id)
        if not project:
            return False

        if project.is_own_contributor(request.user.id):
            return True

        return False
