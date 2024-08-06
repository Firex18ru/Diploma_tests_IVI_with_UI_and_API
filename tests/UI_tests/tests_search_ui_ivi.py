import allure

from Diploma_tests_IVI_with_UI_and_API_tests.models.pages.ivi_main_page import (
    open_main_page, search_muvie, click_on_search, results_message,
    no_results_message
)


@allure.epic("Search page")
class TestSearchPage:

    @allure.story("Поиск конкретного фильма")
    @allure.title("Поиск видео 'Дом Дракона' показывает отсутствие результатов")
    @allure.feature("Поиск фильма")
    @allure.label("Видеопоиск")
    @allure.tag("smoke", "web")
    @allure.severity("normal")
    def test_search_specific_movie(self):
        open_main_page()
        click_on_search()
        search_muvie("Дом Дракона")
        no_results_message()

    @allure.story("Поиск конкретного фильма")
    @allure.title("Поиск видео 'Дом Дракона' показывает альтернативные варианты")
    @allure.feature("Поиск фильма")
    @allure.label("Видеопоиск")
    @allure.tag("smoke", "web")
    @allure.severity("normal")
    def test_search_alternative_movie(self):
        open_main_page()
        click_on_search()
        search_muvie("Дом Дракона")
        results_message()
