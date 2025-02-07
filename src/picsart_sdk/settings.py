import os

PICSART_LOG_HTTP_CALLS = os.environ.get("PICSART_SDK_LOG_HTTP_CALLS", "false") == "true"
PICSART_LOG_HTTP_CALLS_HEADERS = (
    os.environ.get("PICSART_SDK_LOG_HTTP_CALLS_HEADERS", "false") == "true"
)

try:
    DEFAULT_HTTP_TIMEOUT_SECONDS = int(
        os.environ.get("PICSART_SDK_DEFAULT_HTTP_TIMEOUT_SECONDS", 99)
    )
except (ValueError, TypeError):
    DEFAULT_HTTP_TIMEOUT_SECONDS = 99

PICSART_IMAGE_API_VERSION = os.environ.get("PICSART_SDK_IMAGE_API_VERSION", "1.0")
PICSART_IMAGE_GENAI_API_VERSION = os.environ.get(
    "PICSART_SDK_IMAGE_GENAI_API_VERSION", "v1"
)
