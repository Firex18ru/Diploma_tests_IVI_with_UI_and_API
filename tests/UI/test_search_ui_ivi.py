import allure

from ivi_project_tests.pages.ivi_main_page import main_page


@allure.epic("Search page")
class TestSearchPage:

    @allure.story("Поиск конкретного фильма")
    @allure.title("Поиск видео 'Дом Дракона' показывает отсутствие результатов")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("normal")
    def test_search_specific_movie(self):
        main_page.open_main_page()
        main_page.click_on_search()
        main_page.search_muvie("Дом Дракона")
        main_page.no_results_message()

    @allure.story("Поиск конкретного фильма")
    @allure.title("Поиск видео 'Дом Дракона' показывает альтернативные варианты")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("normal")
    def test_search_alternative_movie(self):
        main_page.open_main_page()
        main_page.click_on_search()
        main_page.search_muvie("Дом Дракона")
        main_page.results_message()
