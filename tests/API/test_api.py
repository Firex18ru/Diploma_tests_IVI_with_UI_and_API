import allure

from schemas.ivi_api_schemas import *


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
        expected_titles = ["0-2", "3-4", "5-6", "7-12"]
        actual_titles = [category["title"] for category in response.json()]
        assert set(expected_titles).issubset(set(actual_titles))

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
        expected_title = "3-4"
        actual_titles = [category["title"] for category in response.json()]
        assert expected_title in actual_titles

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
        result = response.json()
        for meta_genre in result:
            assert "id" in meta_genre
            assert "title" in meta_genre
            assert "hru" in meta_genre

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
        result = response.json()["result"]
        for meta_genre in result:
            assert "id" in meta_genre
            assert "title" in meta_genre
            assert "hru" in meta_genre
            assert "priority" in meta_genre

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
        result = response.json()["result"]
        for catalogue in result:
            assert "id" in catalogue
            assert "title" in catalogue
            assert "hru" in catalogue
            assert "years" in catalogue

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
        result = response.json()["result"]
        for catalogue in result:
            assert "id" in catalogue
            assert "title" in catalogue
            assert "hd_available_all" in catalogue
            assert "fullhd_available_all" in catalogue
            assert len([catalogue for catalogue in result if
                        catalogue["hd_available_all"] and catalogue["fullhd_available_all"]]) == len(result)
