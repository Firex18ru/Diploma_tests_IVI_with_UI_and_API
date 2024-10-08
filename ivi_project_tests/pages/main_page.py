from allure import step
from selene import browser, be, by, have


class Main:
    def verify_page_title(self, expected_title):
        with step(f"Проверить заголовок страницы: {expected_title}"):
            browser.element(".headerBar__title").should(be.visible).should(have.text(expected_title))

    def open_main_page(self):
        with step("Открыть главную страницу"):
            browser.open('/')

    def click_on_notifications_button(self):
        with step("Нажать на кнопку уведомлений"):
            browser.element(".headerNotify").should(be.visible).click()

    def verify_notifications_page(self):
        self.verify_page_title("Уведомления")

    def click_ivi_logo(self):
        with step("Нажать на логотип 'Иви'"):
            browser.element(".headerLogo__link").should(be.visible).click()

    def verify_start_page(self):
        with step("Проверить, что открыта стартовая страница"):
            browser.should(have.url("https://www.ivi.tv/"))

    def click_movies_button(self):
        with step("Нажать на кнопку 'Фильмы'"):
            browser.element(by.text("Фильмы")).should(be.visible).click()

    def verify_movies_page_title(self):
        with step("Проверить заголовок на странице 'Фильмы'"):
            self.verify_page_title("Фильмы смотреть онлайн")

    def click_serials_button(self):
        with step("Нажать на кнопку 'Сериалы'"):
            browser.element(by.text("Сериалы")).should(be.visible).click()

    def verify_serials_page_title(self):
        self.verify_page_title("Сериалы смотреть онлайн")

    def click_cartoons_button(self):
        with step("Нажать на кнопку 'Мультфильмы'"):
            browser.element(by.text("Мультфильмы")).should(be.visible).click()

    def verify_cartoons_page_title(self):
        self.verify_page_title("Мультфильмы смотреть онлайн")


main_page = Main()
