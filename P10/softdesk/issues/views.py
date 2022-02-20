from rest_framework.permissions import IsAuthenticated
from authentication.permissions import ProjectContributors, IsIssueAuthorOrReadonly

from softdesk.abstractView import AbstractViewSet

from issues.serializers import IssueListSerializer, IssueDetailSerializer, IssueUpdateSerializer
from issues.models import Issue
from projects.models import Project


class IssueViewSet(AbstractViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    update_serializer_class = IssueUpdateSerializer
    permission_classes = [IsAuthenticated, ProjectContributors, IsIssueAuthorOrReadonly]
    condition_queryset = {
        'project_id': 'project_id_pk'
    }
    _class = Issue

    def get_serializer_class(self):
        if self.action == 'update':
            return self.update_serializer_class

        return super().get_serializer_class()

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs.get('project_id_pk'))
        auto_field = {
            'author_user_id': self.request.user,
            'project_id': project
        }
        if 'assignee_user_id' not in serializer.validated_data.keys():
            auto_field.update({
                'assignee_user_id': self.request.user
            })
        serializer.save(**auto_field)
