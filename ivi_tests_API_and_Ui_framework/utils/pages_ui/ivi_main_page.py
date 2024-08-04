from allure import step
from selene import browser, be, by


def open_main_page():
    with step("Открыть главную страницу"):
        browser.open('/')


def click_on_search():
    with step("Нажать на кнопку поиска"):
        browser.element('[data-test="header_search"]').should(be.visible).click()


def search_muvie(query):
    with step("Выполнить поиск"):
        browser.element('input[data-test="search_input"]').type(query)


def movie_title_should_be_visible():
    element = browser.element(by.css('[data-content-id="16155"]'))
    element.should(be.visible, timeout=10)
