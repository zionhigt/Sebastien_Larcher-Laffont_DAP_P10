from rest_framework.permissions import IsAuthenticated
from authentication.permissions import ProjectContributors, IsCommentAuthorOrReadonly
from softdesk.abstractView import AbstractViewSet
from comments.serializers import CommentListSerializer, CommentDetailSerializer
from comments.models import Comment
from issues.models import Issue


class CommentViewSet(AbstractViewSet):
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated, ProjectContributors, IsCommentAuthorOrReadonly]
    _class = Comment
    condition_queryset = {
        'issue_id': 'issue_id_pk',
    }

    def get_queryset(self):
        records = super().get_queryset()
        project_id = int(self.kwargs.get("project_id_pk"))
        alowed_comments = [
            r.id for r in records
            if r.issue_id.project_id.id == project_id
        ]
        return records.filter(pk__in=alowed_comments)

    def perform_create(self, serializer):
        issue = Issue.objects.get(pk=self.kwargs.get('issue_id_pk'))
        if issue.project_id.id == int(self.kwargs.get('project_id_pk')):
            auto_field = {
                'author_user_id': self.request.user,
                'issue_id': issue
            }
            serializer.save(**auto_field)
