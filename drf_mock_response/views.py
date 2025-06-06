from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from .mixins import FileMockResponseMixin


class MockListAPIView(FileMockResponseMixin, ListAPIView):
    queryset = []
    serializer_class = None


class MockDetailAPIView(FileMockResponseMixin, RetrieveAPIView):
    queryset = []
    serializer_class = None


class MockUpdateAPIView(FileMockResponseMixin, UpdateAPIView):
    queryset = []
    serializer_class = None


class MockDeleteAPIView(FileMockResponseMixin, DestroyAPIView):
    queryset = []
    serializer_class = None
