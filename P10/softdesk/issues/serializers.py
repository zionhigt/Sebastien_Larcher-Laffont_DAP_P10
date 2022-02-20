from rest_framework.serializers import ModelSerializer
from issues.models import Issue


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'priority', 'status', 'project_id', 'author_user_id']


class IssueUpdateSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'priority', 'status', 'assignee_user_id']


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'desc',
            'tag',
            'priority',
            'project_id',
            'date_created',
            'date_updated',
            'status',
            'author_user_id',
            'assignee_user_id',
            'comment_issue'
            ]

        read_only_fields = [
            'id',
            'project_id',
            'date_created',
            'date_updated',
            'author_user_id',
            ]
