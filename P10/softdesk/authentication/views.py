from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

from rest_framework.viewsets import ModelViewSet


class RegisterViewSet(ModelViewSet):
    
    @classmethod
    def as_view(self, *args, **kwargs):
        return super().as_view({'post': "create"})

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer