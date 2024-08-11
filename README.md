# Дипломный проект по автоматизации тестирования сайта "Онлайн кинотеатр IvI"

> <a target="_blank" href="https://www.ivi.ru/">ivi.ru</a>

![main page screenshot](/resources/pictures/base_page_web.jpg)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов
* Запуск API автотестов

### Список проверок, реализованных в web/UI автотестах

- [x] Главная страница сайта отображается
- [x] Проверка логотипа сайта, ведет на главную страницу
- [x] Проверка строки поиска, поиск дает отрицательные результаты
- [x] Проверка строки поиска, поиск предлагает альтернативные варианты
- [x] Проверка кнопки "Уведомления" отображается, открывает окно уведомлений
- [x] Проверка кнопки "Фильмы", открывает окно фильмы
- [x] Проверка кнопки "Сериалы", открывает окно сериалы
- [x] Проверка кнопки "Мультфильмы", открывает окно мультфильмы

### Список проверок, реализованных в API автотестах

- [x] Проверка списка возрастных категорий
- [x] Проверка списка сквозных жанров
- [x] Проверка каталога сборников и единичного контента

----

### Используемый стэк

<img title="Python" src="resources/icon/python-original.svg" height="40" width="40"/><img title="Pytest" src="resources/icon/pytest-original.svg" height="40" width="40"/><img title="Jira" src="resources/icon/jira-original.svg" height="40" width="40"/><img title="Allure Report" src="resources/icon/Allure_Report.png" height="40" width="40"/><img title="Allure TestOps" src="/resources/icon/AllureTestOps.png" height="40" width="40"/><img title="GitHub" src="resources/icon/github.svg" height="40" width="40"/><img title="Selenoid" src="resources/icon/selenoid.png" height="40" width="40"/><img title="Selene" src="resources/icon/selene.svg" height="40" width="40"/><img title="Pycharm" src="resources/icon/pycharm.svg" height="40" width="40"/><img title="Telegram" src="resources/icon/tg.png" height="40" width="40"/><img title="Jenkins" src="resources/icon/jenkins.svg" height="40" width="40"/>

----

### Проект в Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/Diploma_tests_IVI_with_UI_and_API/">Ссылка</a>

#### Проект в Jenkins

* Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Diploma_tests_IVI_with_UI_and_API/">проект</a>

![jenkins project main page](/resources/pictures/jenkins_joba.jpg)

----

### Allure отчет

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Diploma_tests_IVI_with_UI_and_API/19/allure/">Общие результаты</a>

![allure_report_overview](/resources/pictures/allure_statistics.jpg)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Diploma_tests_IVI_with_UI_and_API/21/allure/#suites/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](/resources/pictures/allure_report.jpg)

----

### Интеграция с Allure TestOps

> <a target="_blank" href="https://allure.autotests.cloud/project/4362/dashboards">Ссылка на проект</a>

#### <a target="_blank" href="https://allure.autotests.cloud/project/4362/dashboards">Дашборд с общими показателями тестовых прогонов</a>

![allure_test_ops_dashboards](/resources/pictures/testops_statistics.jpg)

#### <a target="_blank" href="https://allure.autotests.cloud/project/4362/test-cases/33526?treeId=0">Тест кейсы</a>

![allure_testops_suites](/resources/pictures/testops_test_cases.jpg)

#### <a target="_blank" href="https://allure.autotests.cloud/launch/40883/tree/657633/attachments?treeId=0">Результаты тестов</a>

![allure_testops_suites](/resources/pictures/testops_test_result.jpg)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Ручной тест-кейс</a>

![allure_testops_suites](/resources/pictures/testops_manual_test.jpg)

----

### Интеграция с Jira

![jira_project](resources/pictures/jira_test_cases.jpg)

----

### Оповещения в Telegram

![telegram_allert](resources/pictures/tellegram_tests.jpg)

----

### Видео прохождения web/UI автотеста

![autotest_gif](resources/pictures/test_video.gif)

