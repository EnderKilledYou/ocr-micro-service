
import pytest
import json

from app import app


@pytest.fixture(scope='module')
def client():
    flask_app = app
    testing_client = app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


def test_image_upload(client):
    """Make image upload works."""
    with open('test_image.png', 'rb') as test_image:
        data = {
            'image': (test_image, 'test_image.png')
        }
        response = client.post('/ocr', data=data)
        assert(response.status_code,200)
        json_obj = json.loads(response.text)
        assert('success' in json_obj,True)
        assert ('error_message' in json_obj, True)
        assert ('text' in json_obj, True)
        assert(json_obj['success'],True)





