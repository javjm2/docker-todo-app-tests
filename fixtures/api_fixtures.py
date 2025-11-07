import os

import pytest
import requests


def config_requests():
    session = requests.session()

    session.headers.update(
        {
            "accept": "application/json",
            "Authorization": f"Bearer token={os.environ.get('API_KEY')}",
        }
    )
    return session


@pytest.fixture(scope="session")
def custom_requests():
    def wrap():
        return config_requests()

    return wrap


@pytest.fixture
def base_url():
    return os.getenv("BASE_URL", "http://app:3000")


@pytest.fixture
def api_response_error():
    def wrap(response):
        return f"Actual response {response.status_code}: {response.text}"

    return wrap
