import allure

from ivi_project_tests.pages.ivi_main_page import main_page


@allure.epic("Main Page")
class TestMainPage:

    @allure.story("Проверка кнопки уведомлений")
    @allure.title("Проверка отображения и клик на кнопку уведомлений")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_notifications_button(self):
        main_page.open_main_page()
        main_page.click_on_notifications_button()
        main_page.verify_notifications_page()

    @allure.story("Навигация через логотип Иви")
    @allure.title("Проверка перехода через нажатие на логотип Иви на стартовую страницу")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_tv_button(self):
        main_page.open_main_page()
        main_page.click_ivi_logo()
        main_page.verify_start_page()

    @allure.story("Навигация через кнопку 'Фильмы'")
    @allure.title("Проверка перехода на страницу 'Фильмы'")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_movies_button(self):
        main_page.open_main_page()
        main_page.click_movies_button()
        main_page.verify_movies_page_title()

    @allure.story("Навигация и проверка страниц")
    @allure.title("Проверка перехода на страницу 'Сериалы' и возврата на стартовую страницу")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_series_button_and_verify_title(self):
        main_page.open_main_page()
        main_page.verify_start_page()
        main_page.click_serials_button()
        main_page.verify_serials_page_title()

    @allure.story("Навигация и проверка страниц")
    @allure.title("Проверка перехода на страницу 'Мультфильмы'")
    @allure.feature("UI")
    @allure.label("UI Navigation")
    @allure.label("owner", "Yakimenko")
    @allure.tag("smoke", "web")
    @allure.severity("critical")
    def test_cartoons_button_and_verify_title(self):
        main_page.open_main_page()
        main_page.verify_start_page()
        main_page.click_cartoons_button()
        main_page.verify_cartoons_page_title()
