from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator
from contributors.models import Contributors


class ContributorsListSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = [
            'id',
            'user_id',
            'project_id',
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

        validators = [
            UniqueTogetherValidator(
                queryset=Contributors.objects.all(),
                fields=['user_id', 'project_id']
            )
        ]
