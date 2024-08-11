import allure
import pytest
import requests
from jsonschema import validate


@pytest.fixture()
def api_url():
    return "https://api.ivi.ru/mobileapi"


@pytest.fixture()
def api_request_and_validate():
    def _api_request_and_validate(url, params=None, schema=None):
        response = requests.get(url, params=params)
        with allure.step(f"Проверка, API возвращает код статуса 200 для {url}"):
            assert response.status_code == 200
        if schema:
            with allure.step(f"Проверка структуры JSON-ответа для {url}"):
                validate(instance=response.json(), schema=schema)
        return response

    return _api_request_and_validate
