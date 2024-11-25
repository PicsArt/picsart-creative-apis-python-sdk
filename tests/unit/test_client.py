from pytest import fixture

import picsart_sdk

@fixture
def client_name_class_map():
    return {
        "upload": "UploadClient",
        "removebg": "RemoveBackgroundClient",
        "upscale": "UpscaleClient"
    }


def test_client_type(client_name_class_map):
    for client_name, expected_class_name in client_name_class_map.items():
        client = picsart_sdk.client(client_name)
        assert client.__class__.__name__ == expected_class_name, (
            f"Expected {expected_class_name}, but got {client.__class__.__name__} for client '{client_name}'"
        )

def test_client_from_session(client_name_class_map):
    session = picsart_sdk.Session(api_key="API_KEY")
    for client_name, expected_class_name in client_name_class_map.items():
        client = session.client(client_name)
        assert client.__class__.__name__ == expected_class_name, (
            f"Expected {expected_class_name}, but got {client.__class__.__name__} for client '{client_name}'"
        )
