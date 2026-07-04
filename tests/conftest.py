import os
from unittest.mock import MagicMock

# 1. Set environment variables to mock Google Cloud settings
os.environ["GOOGLE_CLOUD_PROJECT"] = "mock-project-id"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

# 2. Mock google.auth.default to bypass local GCP credentials requirement
import google.auth
mock_cred = MagicMock()
mock_cred.quota_project_id = None
mock_cred.token = "mock-token"
google.auth.default = lambda *args, **kwargs: (mock_cred, "mock-project-id")

# 3. Mock google.cloud.logging.Client to avoid connecting to real GCP logging services
import google.cloud.logging
class MockLoggingClient:
    def __init__(self, *args, **kwargs):
        pass
    def logger(self, name):
        mock_logger = MagicMock()
        mock_logger.log_struct = MagicMock()
        return mock_logger

google.cloud.logging.Client = MockLoggingClient
