from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsProjectDetailAccess

from softdesk.abstractView import AbstractViewSet

from projects.serializers import ProjectListSerializer, ProjectDetailSerializer
from projects.models import Project


class ProjectViewSet(AbstractViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectDetailAccess]
    _class = Project

    def get_project_id(self):
        return self.request

    def get_queryset(self):
        records = super().get_queryset()
        alowed_projects = [
            r.id for r in records
            if r.is_own_contributor(self.request.user.id)
        ]
        return records.filter(pk__in=alowed_projects)

    def perform_create(self, serializer):
        auto_field = {
            'author_user_id': self.request.user
        }
        serializer.save(**auto_field)
