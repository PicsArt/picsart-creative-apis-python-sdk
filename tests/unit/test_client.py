import unittest

import picsart_sdk


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client_name_class_map = {
            "upload": "UploadClient",
            "removebg": "RemoveBackgroundClient",
            "upscale": "UpscaleClient"
        }

    def test_client_type(self):
        for client_name, expected_class_name in self.client_name_class_map.items():
            client = picsart_sdk.client(client_name)
            self.assertEqual(client.__class__.__name__, expected_class_name)

    def test_client_from_session(self):
        session = picsart_sdk.Session(api_key="API_KEY")
        for client_name, expected_class_name in self.client_name_class_map.items():
            client = session.client(client_name)
            self.assertEqual(client.__class__.__name__, expected_class_name)
