import json
import os
import time

from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class FileMockResponseMixin:
    json_filename = None
    mock_status = 200
    delay_seconds = 0

    def get_app_name(self):
        return self.__module__.split(".")[0]

    def get_mock_file_path(self):
        if not self.json_filename:
            raise ValueError("json_filename must be defined.")
        app_name = self.get_app_name()
        return os.path.join(settings.BASE_DIR, app_name, "json_mock", self.json_filename)

    def get_mock_data(self):
        file_path = self.get_mock_file_path()
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def finalize_response(self, request, response, *args, **kwargs):
        if self.json_filename:
            time.sleep(self.delay_seconds)
            response = Response(self.get_mock_data(), status=self.mock_status)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}

            return response
        return super().finalize_response(request, response, *args, **kwargs)
