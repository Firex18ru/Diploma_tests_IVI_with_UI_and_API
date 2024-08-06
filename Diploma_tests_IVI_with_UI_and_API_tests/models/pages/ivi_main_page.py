from allure import step
from selene import browser, be, by, have


def open_main_page():
    with step("Открыть главную страницу"):
        browser.open('/')


def click_on_search():
    with step("Нажать на кнопку поиска"):
        browser.element("[data-test='header_search']").should(be.visible).click()


def search_muvie(query):
    with step("Выполнить поиск"):
        browser.element("input[data-test='search_input'']").type(query)


def no_results_message():
    with step("Результаты поиска отсутствуют и отображается соответствующее сообщение"):
        browser.element(by.css(".searchBlock__title")).should(be.visible).should(
            have.text("Ничего не нашлось. Возможно, тебя заинтересует"))


def results_message():
    with step("Альтернативные результаты поиска"):
        browser.element(by.css(".searchBlock__content")).should(be.visible)


def click_on_notifications_button():
    with step("Нажать на кнопку уведомлений"):
        browser.element(".headerNotify").should(be.visible).click()


def verify_notifications_page():
    with step("Провеяем, что открылась страница уведомления"):
        browser.element("h1.headerBar__title").should(be.visible).should(have.text("Уведомления"))


def click_ivi_logo():
    with step("Нажать на логотип 'Иви'"):
        browser.element('div[data-test="header_logo"] a.headerLogo__link').should(be.visible).click()


def verify_start_page():
    with step("Проверить, что открыта стартовая страница"):
        browser.should(have.url("https://www.ivi.tv/"))


def click_movies_button():
    with step("Нажать на кнопку 'Фильмы'"):
        browser.element("//div[contains(@class, 'nbl-button__primaryText') and text()='Фильмы']").should(
            be.visible).click()


def verify_movies_page_title():
    with step("Проверить заголовок на странице 'Фильмы'"):
        browser.element("h1.headerBar__title").should(have.text("Фильмы смотреть онлайн"))


def click_serials_button():
    with step("Нажать на кнопку 'Сериалы'"):
        browser.element("//div[contains(@class, 'nbl-button__primaryText') and text()='Сериалы']").should(
            be.visible).click()

#
def verify_serials_page_title():
    with step("Проверить заголовок на странице 'Сериалы'"):
        browser.element("h1.headerBar__title").should(have.text("Сериалы смотреть онлайн"))


def click_cartoons_button():
    with step("Нажать на кнопку 'Мультфильмы'"):
        browser.element("//div[contains(@class, 'nbl-button__primaryText') and text()='Мультфильмы']").should(
            be.visible).click()


def verify_cartoons_page_title():
    with step("Проверить заголовок на странице 'Мультфильмы'"):
        browser.element("h1.headerBar__title").should(have.text("Мультфильмы смотреть онлайн"))
