import json
import falcon
from falcon import testing
import pytest
import kanda.main


@pytest.fixture
def client():
    app = kanda.main.create_app()
    return testing.TestClient(app)


def test_valid_user(client):
    response = client.simulate_post(
        '/user',
        body=json.dumps({
            "first_name": "ernest",
            "last_name": "appiah",
            "password": "Hello2016~!@#$",
            "email": "ernest@example.com"
        }),
        headers={'content-type': 'application/json'}
    )
    assert response.status == falcon.HTTP_CREATED
    assert response.json == {}


def test_empty_request_body(client):
    EXPECTED_RESPONSE = {
        "field_errors": {
            "password": [
                "Missing data for required field."
            ],
            "email": [
                "Missing data for required field."
            ],
            "first_name": [
                "Missing data for required field."
            ],
            "last_name": [
                "Missing data for required field."
            ]
        },
        "error": "Bad Requests"
    }
    response = client.simulate_post(
        '/user',
        body=json.dumps({}),
        headers={'content-type': 'application/json'}
    )

    assert response.status == falcon.HTTP_400
    assert response.json == EXPECTED_RESPONSE


def test_missing_fields(client):
    EXPECTED_RESPONSE = {
        "field_errors": {
            "last_name": [
                "Missing data for required field."
            ],
            "first_name": [
                "Missing data for required field."
            ],
            "email": [
                "Missing data for required field."
            ]
        },
        "error": "Bad Requests"
    }
    response = client.simulate_post(
        '/user',
        body=json.dumps({"password": "ilovek@12ndA!"}),
        headers={'content-type': 'application/json'}
    )

    assert response.status == falcon.HTTP_400
    assert response.json == EXPECTED_RESPONSE


def test_field_type_incorrect(client):
    EXPECTED_RESPONSE = {
        "field_errors": {
            "first_name": [
                "Not a valid string."
            ]
        },
        "error": "Bad Requests"
    }
    response = client.simulate_post(
        '/user',
        body=json.dumps({
            "first_name": 200,
            "last_name": "appiah",
            "password": "Hello2016~!@#$",
            "email": "ernest@example.com"
        }),
        headers={'content-type': 'application/json'}
    )

    assert response.status == falcon.HTTP_400
    assert response.json == EXPECTED_RESPONSE


def test_password_invalid(client):
    EXPECTED_RESPONSE = {
        "field_errors": {
            "password": [
                "Length must be 8 characters",
                "Password must contain a uppercase character",
                "Password must contain a number",
                "Password must contain a special character [~!@#$%^&*()_+{}\":;']+$",
                "Password must contain a lowercase character"
            ]
        },
        "error": "Bad Requests"
    }
    response = client.simulate_post(
        '/user',
        body=json.dumps({
            "first_name": "ernest",
            "last_name": "appiah",
            "password": "a",
            "email": "ernest@example.com"
        }),
        headers={'content-type': 'application/json'}
    )
    print(response.json)
    assert response.status == falcon.HTTP_400
    assert response.json == EXPECTED_RESPONSE
