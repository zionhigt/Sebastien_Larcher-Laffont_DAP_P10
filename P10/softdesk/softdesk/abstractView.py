from rest_framework.viewsets import ModelViewSet


class AbstractViewSet(ModelViewSet):
    serializer_class = None
    detail_serializer_class = None
    permission_classes = []
    _class = None
    condition_queryset = {}

    def get_queryset(self):
        filter_queryset = {}
        for k, v in self.condition_queryset.items():
            if v in list(self.kwargs.keys()):
                filter_queryset[k] = int(self.kwargs.get(v))
        records = self._class.objects.filter(**filter_queryset)
        return records

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create']:
            return self.detail_serializer_class

        return super().get_serializer_class()
