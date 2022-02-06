from rest_framework.permissions import IsAuthenticated
from authentication.permissions import AuthorOnly

from softdesk.abstractView import AbstractViewSet

from projects.serializers import ProjectListSerializer, ProjectDetailSerializer
from projects.serializers import ProjectListSerializer, ProjectDetailSerializer
from projects.models import Project


class ProjectViewSet(AbstractViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, AuthorOnly]
    _class = Project


