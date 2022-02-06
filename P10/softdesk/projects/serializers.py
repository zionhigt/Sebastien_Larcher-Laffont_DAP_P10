from rest_framework.serializers import ModelSerializer
from projects.models import Project


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title']


class ProjectDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'desc',
            'type',
            'project_contrib',
            'date_created',
            'date_updated',
            'author_user_id',
            ]
