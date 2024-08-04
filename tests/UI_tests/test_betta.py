from ivi_tests_API_and_Ui_framework.utils.pages_ui.ivi_main_page import (
    open_main_page, search_muvie, movie_title_should_be_visible, click_on_search
)


def test_search_specific_movie(setup_browser):
    open_main_page()
    click_on_search()
    search_muvie("Дом Дракона")
    movie_title_should_be_visible()
