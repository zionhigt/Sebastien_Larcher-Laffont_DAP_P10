from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from authentication.permissions import IsProjectAuthorOrReadonly, NotUpdatable

from softdesk.abstractView import AbstractViewSet

from contributors.serializers import ContributorsListSerializer, ContributorsDetailSerializer
from contributors.models import Contributors


class ContributorsViewSet(AbstractViewSet):
    serializer_class = ContributorsListSerializer
    detail_serializer_class = ContributorsDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorOrReadonly, NotUpdatable]
    _class = Contributors
    condition_queryset = {
        'project_id': 'project_id_pk'
    }

    def create(self, request, *args, **kwargs):
        draft_data = request.data.copy()
        draft_data.update({'project_id': self.kwargs.get('project_id_pk')})
        serializer = self.get_serializer(data=draft_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
