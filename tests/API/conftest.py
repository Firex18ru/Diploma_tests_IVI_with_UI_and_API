import allure
import pytest
import requests
from jsonschema import validate
from ivi_project_tests.utils.helper import response_logging, response_attaching

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
        response_logging(response)
        response_attaching(response)
        return response

    return _api_request_and_validate
