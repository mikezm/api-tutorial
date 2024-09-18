import json

from project import create_app


def test_home_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.content_type == 'application/json'
        assert response.is_json == True
        data = json.loads(response.data)
        assert data['message'] == 'Hello World!'