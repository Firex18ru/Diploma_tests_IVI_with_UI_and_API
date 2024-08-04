import allure
import requests
from jsonschema import validate

from tests.API_tests.schemas.ivi_api_schemas import age_categories_schema, all_age_categories_schema, \
    meta_genres_schema, meta_genres_schema_v5_all_params, \
    catalogue_schema_catalogue_genre_and_rating, catalogue_schema_format_and_3d


class Testivi:
    @allure.step("Тестирование получения всех возрастных категорий.")
    def test_get_all_age_categories(self, api_url):
        response = requests.get(f"{api_url}/agecategories/")
        with allure.step("Проверка, API возвращает код статуса 200."):
            assert response.status_code == 200
        json_response = response.json()
        with allure.step("Проверка структуры JSON-ответа."):
            validate(instance=json_response, schema=all_age_categories_schema)

    @allure.step("Тестирование получения возрастных категорий с заданным возрастом.")
    def test_get_age_categories_with_age_only(self, api_url):
        url = f"{api_url}/agecategories/v6/"
        params = {"age": 3}
        response = requests.get(url, params=params)
        with allure.step("Проверка, API возвращает код статуса 200."):
            assert response.status_code == 200
        json_response = response.json()
        with allure.step("Проверка структуры JSON-ответа."):
            validate(instance=json_response, schema=age_categories_schema)

    @allure.step("Тест получения списка сквозных жанров с обязательным параметром app_version.")
    def test_get_meta_genres(self, api_url):
        app_version = 458
        url = f"{api_url}/meta_genres/"
        params = {"app_version": app_version}
        response = requests.get(url, params=params)
        with allure.step("Проверка, API возвращает код статуса 200."):
            assert response.status_code == 200
        data = response.json()
        with allure.step("Проверка структуры JSON-ответа."):
            validate(instance=data, schema=meta_genres_schema)

    @allure.step("Тест получения списка сквозных жанров с использованием всех параметров.")
    def test_get_meta_genres_v5_with_all_params(self, api_url):
        url = f"{api_url}/meta_genres/v5/"
        params = {
            "app_version": 458,
            "country": 1,
            "year_from": 2000,
            "year_to": 2024,
            "category": 10
        }
        response = requests.get(url, params=params)
        with allure.step("Проверка, API возвращает код статуса 200."):
            assert response.status_code == 200
        data = response.json()
        with allure.step("Проверка структуры JSON-ответа."):
            validate(instance=data, schema=meta_genres_schema_v5_all_params)

    @allure.step("Тест каталога с фильтрацией по жанру и рейтингу.")
    def test_get_catalogue_with_genre_and_rating(self, api_url):
        url = f"{api_url}/catalogue/v7/"
        params = {
            "category": 15,
            "genre": 5,
            "ivi_rating_10_gte": 8
        }
        response = requests.get(url, params=params)
        with allure.step("Проверка, API возвращает код статуса 200."):
            assert response.status_code == 200
        data = response.json()
        with allure.step("Проверка структуры JSON-ответа."):
            validate(instance=data, schema=catalogue_schema_catalogue_genre_and_rating)

    @allure.step("Тест каталога с фильтрацией по формату и доступности 3D.")
    def test_get_catalogue_with_format_and_3d(self, api_url):
        url = f"{api_url}/catalogue/v7/"
        params = {
            "category": 15,
            "hd_available": True,
            "3d_available": True
        }
        response = requests.get(url, params=params)
        with allure.step("Проверка, API возвращает код статуса 200."):
            assert response.status_code == 200
        data = response.json()
        with allure.step("Проверка структуры JSON-ответа."):
            validate(instance=data, schema=catalogue_schema_format_and_3d)