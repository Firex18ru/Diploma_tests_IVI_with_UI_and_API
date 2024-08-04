import allure

from ivi_tests_API_and_Ui_framework.utils.pages_ui.ivi_main_page import (
    open_main_page, search_muvie, movie_title_should_be_visible, click_on_search
)


@allure.epic("Base page")
class TestBasePage:

    @allure.story("Search specific movie")
    @allure.title("Search specific movie should return results")
    @allure.feature("Search specific movie")
    @allure.label("Search specific movie")
    @allure.tag("regress", "web")
    @allure.severity("normal")
    def test_search_specific_movie(self, setup_browser):
        open_main_page()
        click_on_search()
        search_muvie("Дом Дракона")
        movie_title_should_be_visible()
