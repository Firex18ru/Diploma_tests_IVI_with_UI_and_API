from allure import step
from selene import browser, be, have


class Search:

    def open_main_page(self):
        with step("Открыть главную страницу"):
            browser.open('/')

    def click_on_search(self):
        with step("Нажать на кнопку поиска"):
            browser.element("[data-test='header_search']").should(be.visible).click()

    def search_movie(self, query):
        with step("Выполнить поиск"):
            browser.element("[data-test='search_input']").type(query)

    def no_results_message(self):
        with step("Результаты поиска отсутствуют и отображается соответствующее сообщение"):
            browser.element(".searchBlock__title").should(be.visible).should(
                have.text("Ничего не нашлось. Возможно, тебя заинтересует"))

    def results_message(self):
        with step("Альтернативные результаты поиска"):
            browser.element(".searchBlock__content").should(be.visible)


search_page = Search()
