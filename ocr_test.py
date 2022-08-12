import pytest
import json

from _pytest.outcomes import fail

from app import app


@pytest.fixture(scope='module')
def client():
    flask_app = app
    testing_client = app.test_client()
    yield testing_client


def test_image_upload(client):
    """Make image upload works."""
    with open('test_image.png', 'rb') as test_image:
        data = {
            'image': (test_image, 'test_image.png')
        }
        response = client.post('/ocr?testing=1', data=data)
        assert (response.status_code, 200)
        json_obj = None
        try:
            json_obj = json.loads(response.text)
        except:
            pass
        assert json_obj is not None
        assert 'success' in json_obj
        assert 'event' in json_obj
        assert 'error_message' in json_obj
        assert 'text' in json_obj
        assert json_obj['success']
        assert len(json_obj['event']) == 1
        assert json_obj['event'][0] == 'google'
