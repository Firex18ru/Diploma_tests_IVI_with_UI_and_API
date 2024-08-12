import allure

from ivi_project_tests.pages.ivi_search_page import search_page


@allure.epic("Search page")
class TestSearchPage:

    @allure.story("Поиск конкретного фильма")
    @allure.title("Поиск видео 'Дом Дракона' показывает отсутствие результатов")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web", "negative")
    @allure.severity("normal")
    def test_search_specific_movie(self):
        search_page.open_main_page()
        search_page.click_on_search()
        search_page.search_movie("Дом Дракона")
        search_page.no_results_message()

    @allure.story("Поиск конкретного фильма")
    @allure.title("Поиск видео 'Дом Дракона' показывает альтернативные варианты")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web", "positive")
    @allure.severity("normal")
    def test_search_alternative_movie(self):
        search_page.open_main_page()
        search_page.click_on_search()
        search_page.search_movie("Дом Дракона")
        search_page.results_message()
