import allure

from ivi_tests_API_and_Ui_framework.utils.pages_ui.ivi_main_page import open_main_page, click_on_notifications_button, \
    verify_notifications_page, verify_start_page, click_ivi_logo, click_movies_button, verify_movies_page_title, \
    verify_serials_page_title, click_serials_button, click_cartoons_button, verify_cartoons_page_title


@allure.epic("Main Page")
class TestMainPage:

    @allure.story("Проверка кнопки уведомлений")
    @allure.title("Проверка отображения и клика на кнопку уведомлений")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_notifications_button(self):
        open_main_page()
        click_on_notifications_button()
        verify_notifications_page()

    @allure.story("Навигация через логотип Иви")
    @allure.title("Проверка перехода через нажатие на логотип Иви на стартовую страницу")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_tv_button(self):
        open_main_page()
        click_ivi_logo()
        verify_start_page()

    @allure.story("Навигация через кнопку 'Фильмы'")
    @allure.title("Проверка перехода на страницу 'Фильмы'")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_movies_button(self):
        open_main_page()
        click_movies_button()
        verify_movies_page_title()

    @allure.story("Навигация и проверка страниц")
    @allure.title("Проверка перехода на страницу 'Сериалы' и возврата на стартовую страницу")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_series_button_and_verify_title(self):
        open_main_page()
        verify_start_page()
        click_serials_button()
        verify_serials_page_title()

    @allure.story("Навигация и проверка страниц")
    @allure.title("Проверка перехода на страницу 'Мультфильмы'")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_cartoons_button_and_verify_title(self):
        open_main_page()
        verify_start_page()
        click_cartoons_button()
        verify_cartoons_page_title()
