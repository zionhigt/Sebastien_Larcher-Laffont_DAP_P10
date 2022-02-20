from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'desc']


class CommentDetailSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'desc',
            'issue_id',
            'date_created',
            'date_updated',
            'author_user_id'
            ]
        read_only_fields = ['issue_id', 'author_user_id', 'date_created', 'date_updated', 'id']
