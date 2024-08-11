import allure

from schemas.ivi_api_schemas import *
from tests.API.helper import response_logging, response_attaching


@allure.epic("API request")
class TestIvi:

    @allure.story("Проверка всех возрастных категорий")
    @allure.title("Тестирование получения всех возрастных категорий")
    @allure.feature("API")
    @allure.label("API request")
    @allure.label("owner", "Yakimenko")
    @allure.tag("regress", "API")
    @allure.severity("normal")
    def test_get_all_age_categories(self, api_url, api_request_and_validate):
        response = api_request_and_validate(
            url=f"{api_url}/agecategories/",
            schema=all_age_categories_schema
        )
        response_logging(response)
        response_attaching(response)

    @allure.story("Проверка возрастных категорий")
    @allure.title("Тестирование получения возрастных категорий с заданным возрастом")
    @allure.feature("API")
    @allure.label("API request")
    @allure.label("owner", "Yakimenko")
    @allure.tag("regress", "API")
    @allure.severity("normal")
    def test_get_age_categories_with_age_only(self, api_url, api_request_and_validate):
        response = api_request_and_validate(
            url=f"{api_url}/agecategories/v6/",
            params={"age": 3},
            schema=age_categories_schema
        )
        response_logging(response)
        response_attaching(response)

    @allure.story("Проверка метаданных жанров")
    @allure.title("Тест получения списка сквозных жанров с обязательным параметром app_version")
    @allure.feature("API")
    @allure.label("API request")
    @allure.label("owner", "Yakimenko")
    @allure.tag("regress", "API")
    @allure.severity("normal")
    def test_get_meta_genres(self, api_url, api_request_and_validate):
        response = api_request_and_validate(
            url=f"{api_url}/meta_genres/",
            params={"app_version": 458},
            schema=meta_genres_schema
        )
        response_logging(response)
        response_attaching(response)

    @allure.story("Проверка метаданных жанров")
    @allure.title("Тест получения списка сквозных жанров с использованием параметров")
    @allure.feature("API")
    @allure.label("API request")
    @allure.label("owner", "Yakimenko")
    @allure.tag("regress", "API")
    @allure.severity("normal")
    def test_get_meta_genres_with_params(self, api_url, api_request_and_validate):
        response = api_request_and_validate(
            url=f"{api_url}/meta_genres/v5/",
            params={
                "app_version": 458,
                "id": 19,
                "title": "Русские",
                "hru": "russkie",
                "priority": 979
            },
            schema=meta_genres_schema_with_params
        )
        response_logging(response)
        response_attaching(response)

    @allure.story("Проверка каталога")
    @allure.title("Тест каталога с использованием параметров")
    @allure.feature("API")
    @allure.label("API request")
    @allure.label("owner", "Yakimenko")
    @allure.tag("regress", "API")
    @allure.severity("normal")
    def test_get_catalogue_with_params(self, api_url, api_request_and_validate):
        response = api_request_and_validate(
            url=f"{api_url}/catalogue/v7/",
            params={
                "category": 16,
                "hru": "muzhskoe-zhenskoe",
                "id": 11063,
                "years": [2016, 2017, 2018],
                "app_version": "1.0"
            },
            schema=catalogue_schema_catalogue_with_params
        )
        response_logging(response)
        response_attaching(response)

    @allure.story("Проверка каталога")
    @allure.title("Тест каталога с фильтрацией по доступному формату")
    @allure.feature("API")
    @allure.label("API request")
    @allure.label("owner", "Yakimenko")
    @allure.tag("regress", "API")
    @allure.severity("normal")
    def test_get_catalogue_to_format_movie(self, api_url, api_request_and_validate):
        response = api_request_and_validate(
            url=f"{api_url}/catalogue/v7/",
            params={
                "category": 14,
                "hd_available_all": True,
                "fullhd_available_all": True
            },
            schema=catalogue_schema_format_movie
        )
        response_logging(response)
        response_attaching(response)
