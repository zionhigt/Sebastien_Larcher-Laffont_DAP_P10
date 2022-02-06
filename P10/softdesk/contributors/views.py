from rest_framework.permissions import IsAuthenticated
from authentication.permissions import AuthorOnly

from softdesk.abstractView import AbstractViewSet

from contributors.serializers import ContributorsListSerializer, ContributorsDetailSerializer
from contributors.models import Contributors


class ContributorsViewSet(AbstractViewSet):
    serializer_class = ContributorsListSerializer
    detail_serializer_class = ContributorsDetailSerializer
    permission_classes = [IsAuthenticated, AuthorOnly]
    _class = Contributors
    condition_queryset = {
        'project_id': 'project_id_pk'
    }


