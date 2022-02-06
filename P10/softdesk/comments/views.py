from rest_framework.permissions import IsAuthenticated
from authentication.permissions import AuthorOnly

from softdesk.abstractView import AbstractViewSet

from comments.serializers import CommentListSerializer, CommentDetailSerializer
from comments.models import Comment


class CommentViewSet(AbstractViewSet):
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated, AuthorOnly]
    _class = Comment
    condition_queryset = {
        'issue_id': 'issue_id_pk'
    }
