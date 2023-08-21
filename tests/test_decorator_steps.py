import allure
from selene import browser, by
from selene.support.conditions import be
from selenium import webdriver
from selene.support.shared.jquery_style import s

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
)


# __________________________________________________________________________
#
# Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
#
# ___________________________________________________________________________

@allure.step("Открываем главну страницу")
def open_main_page():
    browser.open('https://github.com/')


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем tab Issue")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем tab Issue с номером {number}")
def should_see_issue_number(number):
    s(by.partial_text(number)).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_number('81')