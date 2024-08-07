from allure import step
from selene import browser, be, by, have


class Main:

    def open_main_page(self):
        with step("Открыть главную страницу"):
            browser.open('/')

    def click_on_search(self):
        with step("Нажать на кнопку поиска"):
            browser.element("[data-test='header_search']").should(be.visible).click()

    def search_muvie(self, query):
        with step("Выполнить поиск"):
            browser.element("input[data-test='search_input']").type(query)

    def no_results_message(self):
        with step("Результаты поиска отсутствуют и отображается соответствующее сообщение"):
            browser.element(by.css(".searchBlock__title")).should(be.visible).should(
                have.text("Ничего не нашлось. Возможно, тебя заинтересует"))

    def results_message(self):
        with step("Альтернативные результаты поиска"):
            browser.element(by.css(".searchBlock__content")).should(be.visible)

    def click_on_notifications_button(self):
        with step("Нажать на кнопку уведомлений"):
            browser.element(".headerNotify").should(be.visible).click()

    def verify_notifications_page(self):
        with step("Провеяем, что открылась страница уведомления"):
            browser.element("h1.headerBar__title").should(be.visible).should(have.text("Уведомления"))

    def click_ivi_logo(self):
        with step("Нажать на логотип 'Иви'"):
            browser.element('div[data-test="header_logo"] a.headerLogo__link').should(be.visible).click()

    def verify_start_page(self):
        with step("Проверить, что открыта стартовая страница"):
            browser.should(have.url("https://www.ivi.tv/"))

    def click_movies_button(self):
        with step("Нажать на кнопку 'Фильмы'"):
            browser.element("//div[contains(@class, 'nbl-button__primaryText') and text()='Фильмы']").should(
                be.visible).click()

    def verify_movies_page_title(self):
        with step("Проверить заголовок на странице 'Фильмы'"):
            browser.element("h1.headerBar__title").should(have.text("Фильмы смотреть онлайн"))

    def click_serials_button(self):
        with step("Нажать на кнопку 'Сериалы'"):
            browser.element("//div[contains(@class, 'nbl-button__primaryText') and text()='Сериалы']").should(
                be.visible).click()

    def verify_serials_page_title(self):
        with step("Проверить заголовок на странице 'Сериалы'"):
            browser.element("h1.headerBar__title").should(have.text("Сериалы смотреть онлайн"))

    def click_cartoons_button(self):
        with step("Нажать на кнопку 'Мультфильмы'"):
            browser.element("//div[contains(@class, 'nbl-button__primaryText') and text()='Мультфильмы']").should(
                be.visible).click()

    def verify_cartoons_page_title(self):
        with step("Проверить заголовок на странице 'Мультфильмы'"):
            browser.element("h1.headerBar__title").should(have.text("Мультфильмы смотреть онлайн"))


main_page = Main()
