from rest_framework.permissions import IsAuthenticated
from authentication.permissions import AuthorOnly

from softdesk.abstractView import AbstractViewSet

from issues.serializers import IssueListSerializer, IssueDetailSerializer
from issues.models import Issue


class IssueViewSet(AbstractViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticated, AuthorOnly]
    condition_queryset = {
        'project_id': 'project_id_pk'
    }
    _class = Issue

