from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .mixins import FileMockResponseMixin


class MockViewSet(FileMockResponseMixin, ViewSet):
    def list(self, request):
        return Response(self.get_mock_data(), status=self.mock_status)

    def retrieve(self, request, pk=None):
        return Response(self.get_mock_data(), status=self.mock_status)

    def create(self, request):
        return Response(self.get_mock_data(), status=self.mock_status)

    def update(self, request, pk=None):
        return Response(self.get_mock_data(), status=self.mock_status)

    def destroy(self, request, pk=None):
        return Response(self.get_mock_data(), status=self.mock_status)
