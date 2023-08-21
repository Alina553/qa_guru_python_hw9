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

def test_dynamic_steps():
    with allure.step("Открываем главну страницу"):
        browser.open('https://github.com/')

    with allure.step("Ищем репозиторий"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step("Переходим по ссылке eroshenkoam/allure-example"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем tab Issue"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 81"):
        s(by.partial_text("#81")).should(be.visible)

