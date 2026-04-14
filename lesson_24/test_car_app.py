from requests.auth import HTTPBasicAuth
import requests
import pytest
import logging

logger = logging.getLogger("car_tests")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("lesson_24/test_search.log")
file_handler.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


BASE_URL = 'http://127.0.0.1:8080'


def login(session, username, password):
    try:
        url = f'{BASE_URL}/auth'
        response = session.post(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            logger.info(f"Login successful: {response.status_code}")
            return response
        else:
            logger.error(f"Login failed: {response.status_code}")
    except Exception as e:
        logger.error(e)


def get_access_token(response):
    try:
        return response.json().get('access_token')
    except Exception as e:
        logger.error(e)


def set_up_session(session, username, password):
    try:
        access_token = get_access_token(login(session, username, password))
        session.headers.update({"Authorization": f"Bearer {access_token}"})
    except Exception as e:
        logger.error(e)


def get_cars(session, sort_by = None, limit = None):
    url = f'{BASE_URL}/cars'
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit
    return session.get(url, params=params)

@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    set_up_session(session, 'test_user', 'test_pass')
    return session


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("brand", 1),
        ("year", 2),
        ("engine_volume", 3),
        ("price", 5),
        ("price", 2),
        ("engine_volume", 3),
        ("engine_volume", 1)
    ]
)
def test_get_cars(auth_session, sort_by, limit):
    logger.info(f"Request: sort_by={sort_by}, limit={limit}")
    response = get_cars(auth_session, sort_by, limit)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    logger.info("Response is list: OK")
    if limit is not None:
        assert len(data) <= limit
        logger.info("Length of list equal to limit")
    if sort_by is not None:
        values = [car.get(sort_by) for car in data if car.get(sort_by) is not None]
        assert values == sorted(values)
        logger.info("List is correctly sorted")