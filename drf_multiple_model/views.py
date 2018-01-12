from drf_multiple_model.mixins import FlatMultipleModelMixin, ObjectMultipleModelMixin

from rest_framework.generics import GenericAPIView


class FlatMultipleModelAPIView(FlatMultipleModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ObjectMultipleModelAPIView(ObjectMultipleModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
