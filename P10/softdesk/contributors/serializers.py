from rest_framework.serializers import ModelSerializer
from contributors.models import Contributors


class ContributorsListSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = [
            'id',
            'user_id',
            'permission',
            'role'
            ]


class ContributorsDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Contributors
        fields = [
            'id',
            'user_id',
            'project_id',
            'permission',
            'role'
            ]